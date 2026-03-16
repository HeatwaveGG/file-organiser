import os, shutil
from all_file_types import file_types

unoragnised_files_folder = input("Enter path to unorganised files : ")
organised_files_folder = input("Enter path to organised files : ")

files = os.listdir(unoragnised_files_folder)

def find_key_by_value_item(dict, item):
    for key, values in dict.items():
        if item in values:
            return key

for file in files:
    name, extension = os.path.splitext(file)
    moved = False
    for file_type in file_types.values():
        if extension in file_type:
            folder_name = find_key_by_value_item(file_types, extension)
            dest_folder = os.path.join(organised_files_folder, folder_name)
            os.makedirs(dest_folder, exist_ok=True)
            shutil.move(
                os.path.join(unoragnised_files_folder, file),
                os.path.join(dest_folder, file)
            )
            moved = True
            break
    if not moved:
        # Move to "Other" folder
        dest_folder = os.path.join(organised_files_folder, "Other")
        os.makedirs(dest_folder, exist_ok=True)
        shutil.move(
            os.path.join(unoragnised_files_folder, file),
            os.path.join(dest_folder, file)
        )

print ("Done")