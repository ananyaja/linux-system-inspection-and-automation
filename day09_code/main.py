
"""
Master Orchestration Script - Day 09: System Automation Pipeline
Description: Executes workspace inspection, file organization, and telemetry logging sequentially.
"""

from inspector import inspect_workspace_deep
from organizer import organize_directory
from telemetry import log_system_telemetry

def run_pipeline():
    print("==================================================")
    print("STARTING DAY 09 SYSTEM AUTOMATION PIPELINE")
    print("==================================================\n")
    
    # Step 1: Inspect repository structure and workspace health
    print("[Step 1/3] Running Deep Workspace Inspection...")
    inspect_workspace_deep()
    
    print("\n" + "-"*50 + "\n")
    
    # Step 2: Organize loose files into structured categories
    print("[Step 2/3] Running File Organization...")
    organize_directory()
    
    print("\n" + "-"*50 + "\n")
    
    # Step 3: Capture system telemetry and write execution logs
    print("[Step 3/3] Generating System Telemetry Logs...")
    log_system_telemetry()
    
    print("\n==================================================")
    print("PIPELINE EXECUTION COMPLETE")
    print("==================================================")

if __name__ == "__main__":
    run_pipeline()