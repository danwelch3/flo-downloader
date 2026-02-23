import re
import subprocess
import sys
from urllib.parse import urlparse, parse_qs

import requests


def get_api_domain(url):
    """Derive the API domain from the input URL (e.g. flowrestling.org -> api.flowrestling.org)."""
    parsed = urlparse(url)
    hostname = parsed.hostname or ''
    # Strip 'www.' prefix if present
    if hostname.startswith('www.'):
        hostname = hostname[4:]
    return f"api.{hostname}"


def extract_video_id(url):
    """Extract the video ID from a Flo URL.

    Supports both direct video URLs and event pages with a ?playing= param.
    """
    parsed = urlparse(url)
    query_params = parse_qs(parsed.query)

    # Event pages pass the video ID as ?playing=<id>
    if 'playing' in query_params:
        return query_params['playing'][0]

    # Direct video URLs: /video/<id>-<slug>
    path_match = re.search(r'/video/(\d+)', parsed.path)
    if path_match:
        return path_match.group(1)

    # Fallback: first number in the path
    nums = re.findall(r'\d+', parsed.path)
    if nums:
        return nums[0]

    print(f"Error: could not extract video ID from URL: {url}")
    sys.exit(1)


def get_cdn_url(api_domain, cdn_video_id):
    try:
        response = requests.get(
            url=f"https://{api_domain}/api/right-rail/videos/{cdn_video_id}",
        )
        print(f"Response HTTP Status Code: {response.status_code}")
    except requests.exceptions.RequestException:
        print('HTTP Request failed')
        sys.exit(1)

    try:
        return response.json()['data']['source_video']['playlist']
    except (KeyError, TypeError) as e:
        print(f"Error: unexpected API response structure: {e}")
        print(f"Response body: {response.text[:500]}")
        sys.exit(1)


def extract_filename(url):
    """Derive a sensible default filename from the URL."""
    parsed = urlparse(url)
    query_params = parse_qs(parsed.query)

    # For event URLs with ?playing=, use the event slug + video ID
    if 'playing' in query_params:
        # e.g. /events/14829511-2026-chsaa-.../videos -> take the event slug
        parts = parsed.path.strip('/').split('/')
        if len(parts) >= 2:
            return f"{parts[1]}-{query_params['playing'][0]}"
        return query_params['playing'][0]

    # For direct video URLs: /video/<slug>
    parts = parsed.path.strip('/').split('/')
    if len(parts) >= 2:
        return parts[1]

    return parts[0] if parts else 'output'


def main():
    if len(sys.argv) < 2:
        print("Usage: floh4x <flo-video-url> [output-filename]")
        sys.exit(1)

    url = sys.argv[1]
    location_to_save = sys.argv[2] if len(sys.argv) > 2 else extract_filename(url)
    if location_to_save.endswith('.mp4'):
        location_to_save = location_to_save[:-4]

    video_id = extract_video_id(url)
    api_domain = get_api_domain(url)
    print(f"Video ID: {video_id}")
    print(f"API domain: {api_domain}")

    cdn_url = get_cdn_url(api_domain, video_id)

    command = f'ffmpeg -i {cdn_url} -bsf:a aac_adtstoasc -c copy {location_to_save}.mp4'
    subprocess.call(command, shell=True)

    print('Successfully saved video as', f'{location_to_save}.mp4')


if __name__ == '__main__':
    main()
