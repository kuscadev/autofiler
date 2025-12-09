# AutoFiler - Automatic File Organizer
# Copyright (C) 2025 kuscadev
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

import os
import shutil

DIR_TYPES = {
    "Images": (".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg", ".tiff"),
    "Documents": (".pdf", ".docx", ".doc", ".txt", ".xlsx", ".csv", ".pptx"),
    "Archives": (".zip", ".rar", ".7z", ".tar", ".gz", ".iso"),
    "Setup_Files": (".exe", ".msi", ".deb", ".sh", ".AppImage", ".apk"),
    "Videos": (".mp4", ".mkv", ".avi", ".mov", ".flv", ".webm"),
    "Music": (".mp3", ".wav", ".flac", ".aac", ".ogg"),
    "Code_Files": (".py", ".java", ".cpp", ".html", ".css", ".js")
}

home_dir = os.path.expanduser("~")
BASE_DIR = os.path.join(home_dir, "Downloads")

if not os.path.exists(BASE_DIR):
    print(f"ERROR: {BASE_DIR} not found!")
    exit()
print(f"Target Directory: {BASE_DIR}")
print("-" * 40)

for filename in os.listdir(BASE_DIR):
    file_path = os.path.join(BASE_DIR, filename)
    if os.path.isdir(file_path):
        continue
    if filename.startswith("."):
        continue
    filename_lower = filename.lower()
    moved = False
    for folder_name, extensions in DIR_TYPES.items():
        if filename_lower.endswith(extensions):
            target_folder = os.path.join(BASE_DIR, folder_name)
            if not os.path.exists(target_folder):
                os.mkdir(target_folder)
                print(f"New folder created: {target_folder}")
            target_path = os.path.join(target_folder, filename)
            try:
                shutil.move(file_path, target_path)
                print(f"Moved: {filename} -> {folder_name}")
                moved = True
                break
            except Exception as e:
                print(f"Error: ({filename}): {e}")