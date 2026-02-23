# floh4x
Download videos off FloSports CDN (flograppling, flowrestling, and other Flo sites)

## Requirements

- [ffmpeg](http://jollejolles.com/install-ffmpeg-on-mac-os-x/) installed on your computer
- Python 3.8+

## Usage

```
floh4x <flo-video-url> [output-filename]
```

The optional `output-filename` argument lets you choose the name of the saved `.mp4` file. If omitted, the filename is derived from the URL slug. The `.mp4` extension is added automatically (but accepted if provided).

Supports both direct video URLs and event pages with a `?playing=` parameter:

```
# Direct video URL
floh4x https://www.flograppling.com/video/6458762-levi-jones-leary-vs-oliver-lovell

# Event page with playing param
floh4x https://www.flowrestling.org/events/14829511-2026-chsaa-co-state-championships/videos?playing=15465329
```

## Quick Start (uvx)

The easiest way to run floh4x is with [uv](https://docs.astral.sh/uv/):

```
uvx --from git+https://github.com/danwelch3/flo-downloader floh4x https://www.flograppling.com/video/6458762-levi-jones-leary-vs-oliver-lovell-abu-dhabi-world-professional-jiu-jitsu-championship
```

With a custom filename:

```
uvx --from git+https://github.com/danwelch3/flo-downloader floh4x https://www.flograppling.com/video/6458762-levi-jones-leary-vs-oliver-lovell-abu-dhabi-world-professional-jiu-jitsu-championship levi-vs-lovell
```

## Run from Local Clone

```bash
git clone https://github.com/danwelch3/flo-downloader.git
cd flo-downloader
pip install -Ur requirements.txt
python main.py https://www.flograppling.com/video/6458762-levi-jones-leary-vs-oliver-lovell-abu-dhabi-world-professional-jiu-jitsu-championship
```

The video will be saved as `6458762-levi-jones-leary-vs-oliver-lovell-abu-dhabi-world-professional-jiu-jitsu-championship.mp4` in the current directory, or as the custom filename if one was provided.
