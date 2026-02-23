import re
import subprocess
import sys

import requests


def get_cdn_url(cdn_video_id):
    try:
        response = requests.get(
            url=f"https://api.flograppling.com/api/right-rail/videos/{cdn_video_id}",
        )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')

    return response.json()['data']['source_video']['playlist']


def main():
    if len(sys.argv) < 2:
        print("Usage: floh4x <flograppling-video-url> [output-filename]")
        sys.exit(1)

    url = sys.argv[1]
    location_to_save = sys.argv[2] if len(sys.argv) > 2 else url.split('/')[4]
    if location_to_save.endswith('.mp4'):
        location_to_save = location_to_save[:-4]
    video_id = re.findall(r'\d+', url)[0]
    cdn_url = get_cdn_url(video_id)

    command = f'ffmpeg -i {cdn_url} -bsf:a aac_adtstoasc -c copy {location_to_save}.mp4'
    subprocess.call(command, shell=True)

    print('Successfully saved FloGrappling video as', f'{location_to_save}.mp4')


if __name__ == '__main__':
    main()
