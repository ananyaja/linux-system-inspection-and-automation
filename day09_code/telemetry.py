"""
Module: Telemetry
Description: Captures system path environment and runtime diagnostic logs.
"""

import sys
import os
from pathlib import Path
from datetime import datetime

def log_system_telemetry(log_filename: str = "system_telemetry.log") -> None:
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_path = Path(log_filename)
    
    telemetry_data = [
        f"=== SYSTEM TELEMETRY REPORT ===",
        f"Timestamp: {timestamp}",
        f"Python Version: {sys.version}",
        f"Platform: {sys.platform}",
        f"Current Working Directory: {os.getcwd()}",
        f"Environment PATH entries: {len(os.environ.get('PATH', '').split(os.pathsep))}",
        f"=" * 30 + "\n"
    ]
    
    report_text = "\n".join(telemetry_data)
    log_path.write_text(report_text, encoding="utf-8")
    print(report_text)
    print(f"Telemetry log successfully written to: {log_path.absolute()}")

if __name__ == "__main__":
    log_system_telemetry()