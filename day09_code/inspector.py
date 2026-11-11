"""
Module: Inspector
Description: Recursively inspects workspace directories and locates Git repositories.
"""

from pathlib import Path
from datetime import datetime

def inspect_workspace_deep(target_dir: str = r"C:\projects") -> None:
    root_path = Path(target_dir)
    if not root_path.exists():
        print(f"Error: Directory {target_dir} does not exist.")
        return

    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"[{timestamp}] Deep Inspecting workspace: {root_path}\n")
    
    repos = []
    file_counts = {}
    total_size_bytes = 0

    # Locate every Git repository recursively
    for git_path in root_path.rglob(".git"):
        if git_path.is_dir():
            repo_dir = git_path.parent
            repos.append(repo_dir.relative_to(root_path))

    # Tally loose files in root
    for item in root_path.iterdir():
        if item.is_file():
            ext = item.suffix.lower() or "no_extension"
            file_counts[ext] = file_counts.get(ext, 0) + 1
            total_size_bytes += item.stat().st_size

    # Summary Report
    print("=" * 50)
    print("WORKSPACE INSPECTION REPORT")
    print("=" * 50)
    print(f"Total Local Repositories Found: {len(repos)}")
    print("Discovered Repositories:")
    for repo in sorted(repos):
        print(f"  [REPO] {repo}")
        
    print(f"\nRoot Workspace Size (loose files): {total_size_bytes / (1024*1024):.2f} MB")
    print("Root File Extensions Breakdown:")
    for ext, count in sorted(file_counts.items(), key=lambda x: x[1], reverse=True):
        print(f"  - {ext}: {count} file(s)")
    print("=" * 50)

if __name__ == "__main__":
    inspect_workspace_deep()