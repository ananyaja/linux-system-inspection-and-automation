"""
Gradio Web App - Day 09: System Telemetry & Log Inspector
Description: Provides a web interface to process, analyze, and format system diagnostic logs.
"""

import gradio as gr
from datetime import datetime

def analyze_system_log(raw_log_text: str) -> str:
    """
    Simulates parsing and formatting raw telemetry or workspace logs.
    """
    if not raw_log_text.strip():
        return "Error: Please provide valid log content to analyze."

    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    lines = raw_log_text.strip().split("\n")
    line_count = len(lines)

    analysis = [
        f"=== HUGGING FACE TELEMETRY ANALYSIS ===",
        f"Processed at: {timestamp}",
        f"Total Log Lines Analyzed: {line_count}",
        f"Status: Clean and Parsed Successfully",
        "-" * 40,
        "EXTRACTED CONTENT SUMMARY:",
    ]

    for i, line in enumerate(lines[:10], 1):
        analysis.append(f"  [{i}] {line}")

    if line_count > 10:
        analysis.append(f"  ... and {line_count - 10} more line(s).")

    return "\n".join(analysis)

# Build the Gradio UI
demo = gr.Interface(
    fn=analyze_system_log,
    inputs=gr.Textbox(lines=8, label="Paste System Telemetry or Log Text", placeholder="Paste your log text here..."),
    outputs=gr.Textbox(label="Analysis Report"),
    title="Day 09: System Telemetry Inspector",
    description="A lightweight cloud utility to parse, inspect, and summarize system logs via Gradio."
)


if __name__ == "__main__":
    demo.launch(share=True)