from songs_data_read import songs_read
from songs_data_write import songs_write

print("Welcome to Music Manager!")
root_path = input("Music folder (ex: /home/user/Music/): ")
print("What do you want to do?")
print("0 - import data from songs to excel")
print("1 - update songs data from excel")
choice = int(input("Option: "))

if choice == 0:
    songs_read(root_path)
elif choice == 1:
    songs_write(root_path)
else:
    print("Error! Input not supported.")

