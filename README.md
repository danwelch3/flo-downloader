# floh4x
Download videos off flograppling CDN

## Requirements

- [ffmpeg](http://jollejolles.com/install-ffmpeg-on-mac-os-x/) installed on your computer
- Python 3.8+

## Quick Start (uvx)

The easiest way to run floh4x is with [uv](https://docs.astral.sh/uv/):

```
uvx --from git+https://github.com/danwelch3/flo-downloader floh4x https://www.flograppling.com/video/6458762-levi-jones-leary-vs-oliver-lovell-abu-dhabi-world-professional-jiu-jitsu-championship
```

## Run from Local Clone

```bash
git clone https://github.com/danwelch3/flo-downloader.git
cd flo-downloader
pip install -Ur requirements.txt
python main.py https://www.flograppling.com/video/6458762-levi-jones-leary-vs-oliver-lovell-abu-dhabi-world-professional-jiu-jitsu-championship
```

The video will be saved as `6458762-levi-jones-leary-vs-oliver-lovell-abu-dhabi-world-professional-jiu-jitsu-championship.mp4` in the current directory.
