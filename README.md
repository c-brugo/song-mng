# song-mng
`song-mng` is a linux manager for music files and song metadata written in python.

Right now, two main tasks are present:
 - **task 0**: copy of the metadata of mp3 files present in a folder to an Excel file `songs.xlsx`, where are easy to edit
 - **task 1**: application of the changes written in `songs.xlsx` to the mp3 files

The data as now covered and editable are:
 - File name
 - Title of the song
 - Artist
 - Album
 - Album Artist

## Usage
 - Download the repository
 - Run the file `song-mng.py`
 - If `songs.xlsx` not present or new files added, execute task 0
 - Edit data in `songs.xlsx`
 - Apply changes with task 1

# Tech
App developed with Python v3.8.5.

Relevant packages used
 - [`openpyxl`](https://openpyxl.readthedocs.io/en/stable/) (v3.0.5): library to read/write Excel 2010 xlsx/xlsm/xltx/xltm files
 - [`eyed3`](https://eyed3.readthedocs.io/en/latest/) (v0.9.4): tool for working with audio files, specifically MP3 files containing ID3 metadata (i.e. song info)

# License
**GPL-3.0 License**