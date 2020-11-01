import eyed3 as e3
import os, json
from openpyxl import Workbook
from openpyxl.styles import colors
from openpyxl.styles import Font, Color

#base functions
def type_mp3(name):
    return name.endswith(".mp3")

def auto_size(worksheet):
    for col in worksheet.columns:
        max_length = 0
        column = col[0].column_letter # Get the column number
        for cell in col:
            try: # Necessary to avoid error on empty cells
                if len(str(cell.value)) > max_length:
                    max_length = len(cell.value)
            except:
                pass
        adjusted_width = (max_length + 2) * 1.2
        worksheet.column_dimensions[column].width = adjusted_width
    #adjust dimension



def songs_read(root_path):
    #file_list extraction
    
    files_list = os.listdir(root_path)

    songs_list = list(filter(type_mp3, files_list))

    #export data to excel file
    wb = Workbook()
    ws = wb.active

    ws.title = "Songs"
    ws.freeze_panes = "A4"

    #Column names
    ws.append(["", "Total songs: ", len(songs_list)])
    ws.append([""])
    ws.append(["id", "File name", "Title", "Artist", "Album", "Album Artist"])

    for song in songs_list:
        song_info = [""] * 6
        song_file = e3.load(root_path + song)
        
        song_info[0] = song
        song_info[1] = song
        song_info[2] = song_file.tag.title
        song_info[3] = song_file.tag.artist
        song_info[4] = song_file.tag.album
        song_info[5] = song_file.tag.album_artist

        ws.append(song_info)

    #Editing
    ws.row_dimensions[3].font = Font(name="Calibri", size=12, bold=True)
    auto_size(ws)
    ws.column_dimensions['A'].hidden= True

    wb.save(root_path + "songs.xlsx")

    print("File 'songs.xlsx' generated")
