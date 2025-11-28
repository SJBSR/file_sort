# Code to sort files in a directory by their file types

import os
import shutil
# Define the extensions to be sorted
directory = os.path.join(os.path.expanduser("~"), "Downloads")
extensions = {
    ".jpg": "Images",
    ".jpeg": "Images",
    ".gif": "Images",
    ".mp4": "Videos",
    ".mov": "Videos",
    ".doc": "Documents",
    ".pdf": "Documents",
    ".txt": "Documents",
    ".mp3": "Music",
    ".wave": "Music",
}
# Iterate through files in the directory
for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)

    if os.path.isfile(file_path):
        extension = os.path.splitext(filename)[1].lower()

    if extension in extensions:
        folder_name = extensions[extension]

        folder_path = os.path.join(directory, folder_name)
        os.makedirs(folder_path, exist_ok=True)

        destination_path = os.path.join(folder_path, filename)
        shutil.move(file_path), (destination_path)

        print(f"Moved {filename} to {folder_name} folder.")
    else:
        print(f"Skipped {filename}, Unknown file extension.")
else:
    print(f"Skipped {filename}, Not a file.")

    print("File sorting completed.")
