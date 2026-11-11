<<<<<<< HEAD

# 🐧 Linux Command Line & Server Inspection Basics (Day 01)

Welcome to **Day 01** of the technical self-study series! Today focuses on mastering core Linux terminal commands used to monitor system resources, check disk space, inspect memory, and manage interactive processes on a cloud virtual machine (Google Colab / Ubuntu).

---

## 🛠️ Core Topics & Commands Covered

### 1. System Resource & Disk Monitoring (`df` & `du`)
* **`df -h`**: Reports free and used disk space on mounted file systems in a human-readable format (`-h` converts raw bytes to GB/MB).
* **`df -T`**: Displays file system types (e.g., `ext4`, `tmpfs`, `overlay`) in a dedicated column.
* **`df -i`**: Inspects inode usage (number of files/directories) instead of storage blocks.
* **`df -t` / `df -x`**: Filter outputs to include or exclude specific file system types.
* **`du -sh`**: Measures the total size of specific directories and files recursively.

### 2. Memory & Process Inspection (`free`, `top`, & `htop`)
* **`free -h`**: Displays total, used, free, and available physical RAM and swap space.
* **`top`**: Real-time terminal utility to view system loads, CPU percentages (`%CPU`), and RAM consumption (`%MEM`).
* **`htop`**: An enhanced interactive, color-coded process viewer.
* **`ps aux --sort=-%mem`**: Lists processes sorted by highest memory usage in a clean text format.

### 3. Process Management & Safety (`kill` & Mount Points)
* **`kill -15 <PID>`**: Sends a graceful termination signal (`SIGTERM`) allowing processes to close safely.
* **`kill -9 <PID>`**: Force-kills unresponsive processes (`SIGKILL`).
* **Mount Point Inspection**: Using `df -h`, `mount`, and `/proc/mounts` to verify active storage attachments (like Google Drive via FUSE).

---

## 📂 Repository Structure
* `day01_linux_inspection.ipynb`: Complete Google Colab notebook containing executable code blocks, live outputs, and detailed markdown notes for every command.
* `README.md`: Documentation and guide for Day 01.

---

## 🚀 How to Run
1. Open the `.ipynb` file in **[Google Colab](https://colab.research.google.com/)**.
2. Run the cells sequentially to observe real-time resource allocation, monitor system memory, and practice safe process management.
=======
---
title: System Telemetry Inspector
emoji: 😻
colorFrom: yellow
colorTo: blue
sdk: gradio
sdk_version: 6.31.0
python_version: '3.12'
app_file: app.py
pinned: false
license: mit
short_description: A minimalist real-time system telemetry and resource monitor
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference
>>>>>>> b5b3a51b4d9efc3fde19feacfdcffed0243706bf
