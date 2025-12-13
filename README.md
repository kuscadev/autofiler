
# AutoFiler

**AutoFiler** is a lightweight, efficient Python automation script designed to organize cluttered directories instantly. It scans your `Downloads` folder (or any target directory) and categorizes files into subfolders based on their extensions.

> "Turn chaos into order with a single command."

---

## Features

* **Dynamic Path Detection:** Automatically detects the user's home directory and locates the `Downloads` folder on Linux, Windows, and macOS.
* **Smart Categorization:** Uses a dictionary-based mapping system to sort files into specific categories (Images, Documents, Archives, etc.).
* **Safe Execution:**
    * Skips hidden files (dotfiles) and existing directories.
    * Includes `try-except` blocks to handle permission errors or file conflicts gracefully.
    * Checks if the target folder exists before attempting operations.
* **Universal Compatibility:** Uses `os.path.join` for cross-platform compatibility.

---

## How It Works

**Before:**
```text
Downloads/
├── homework.docx
├── vacation.jpg
├── installer.exe
├── song.mp3
└── archive.zip
```

**After Running AutoFiler:**

```text
Downloads/
├── Documents/
│   └── homework.docx
├── Images/
│   └── vacation.jpg
├── Setup_Files/
│   └── installer.exe
├── Music/
│   └── song.mp3
└── Archives/
    └── archive.zip
```

-----

## Installation & Usage

### 1\. Clone the Repository

```bash
git clone https://github.com/kuscadev/autofiler.git
cd autofiler
```

   - (For Linux) Run the installer:

        ```Bash
        chmod +x install.sh
        ./install.sh
        ```

        Now you can run it from anywhere by typing `autofiler`.

### 2\. Run the Script

No external libraries required\! It runs on standard Python 3 libraries (`os`, `shutil`).

```bash
python3 autofiler.py
```

### 3\. Customize (Optional)

You can modify the `DIR_TYPES` dictionary in `autofiler.py` to add new extensions or change folder names:

```python
DIR_TYPES = {
    "Images": (".jpg", ".png", ".gif"),
    "My_Project_Files": (".blend", ".psd") # Add your own rules!
}
```

-----

<div align="center">

  **Minimal. Practical. Worth Sharing.**
  
  <sub>© 2025 kusca.dev — Licensed under GPLv3
</sub>

</div>