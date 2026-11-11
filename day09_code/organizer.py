"""
Module: Organizer
Description: Automatically organizes loose files into categorized subfolders.
"""

from pathlib import Path
import shutil

EXTENSION_MAPPING = {
    "code": [".py", ".js", ".sh", ".ps1", ".ipynb"],
    "documents": [".md", ".txt", ".pdf", ".docx", ".csv"],
    "archives": [".zip", ".tar", ".gz", ".rar"],
    "configs": [".json", ".yaml", ".yml", ".env", ".ini"]
}

def organize_directory(target_dir: str = r"C:\projects\code") -> None:
    root_path = Path(target_dir)
    if not root_path.exists():
        print(f"Error: Directory {target_dir} does not exist.")
        return

    print(f"Organizing loose files in: {root_path}\n")
    moved_count = 0

    for item in root_path.iterdir():
        if item.is_file() and item.name != __file__:
            ext = item.suffix.lower()
            category = "misc"
            
            for cat, exts in EXTENSION_MAPPING.items():
                if ext in exts:
                    category = cat
                    break
            
            target_folder = root_path / category
            target_folder.mkdir(exist_ok=True)
            
            destination = target_folder / item.name
            shutil.move(str(item), str(destination))
            print(f"  [Moved] {item.name} -> {category}/")
            moved_count += 1

    print(f"\nSuccessfully organized {moved_count} file(s).")

if __name__ == "__main__":
    organize_directory()