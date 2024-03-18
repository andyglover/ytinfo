# ytinfo

A simple Python script that prompts for a list of YouTube video URLs, separated by new lines, and returns the channel name, title, runtime, and URL of each to the clipboard.

I use a text editor for notetaking and I like to format my notes this way. I found it time-consuming to copy this information from each YouTube video page. 

This script makes use of [PyTube](https://github.com/pytube/pytube), [Pyperclip](https://github.com/asweigart/pyperclip), and [urllib](https://github.com/node-modules/urllib).

## Dependencies

- Python 3.x
- PyTube (>= 11.0.0)
- Pyperclip (>= 1.8.2)
- urllib (>= 3.9.2)

### Installation

1. Make sure you have Python 3.x installed on your system.
2. Install required dependencies using pip:

```bash
pip install pytube pyperclip urllib
```

### Usage

1. Open a terminal or command prompt.
2. Navigate to the directory where the script is located.
3. Run the script using Python:

``` bash
python ytinfo.py
```

4. When prompted, input a video URL, or paste a list of URLs.
5. Hit enter to advance to the next line, where you can add another URL, or press Enter again to finish.
6. The script will then retrieve the channel name, title, runtime, and sanitized URL for each video and copy the information to your clipboard.
