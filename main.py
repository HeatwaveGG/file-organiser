import os, shutil

unoragnised_files_folder = input("Enter path to unorganised files : ")
organised_files_folder = input("Enter path to organised files : ")

file_types = {
    "Image": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg", ".webp"],
    "Video": [".mp4", ".avi", ".mov", ".wmv", ".flv", ".mkv", ".webm", ".mpeg"],
    "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg", ".wma", ".m4a"],
    "Document": [".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt", ".xls", ".xlsx", ".ppt", ".pptx"],
    "Archive": [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".iso"],
    "Database": [".db", ".sqlite", ".mdb", ".accdb", ".sql", ".csv"],
    "Code": [".py", ".js", ".java", ".cpp", ".c", ".cs", ".html", ".css", ".php", ".rb", ".go", ".ts"],
    "Executable": [".exe", ".msi", ".bat", ".sh", ".apk", ".app"],
    "Presentation": [".ppt", ".pptx", ".key", ".odp"],
    "Spreadsheet": [".xls", ".xlsx", ".ods",],
    "No extension": [""]
}

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