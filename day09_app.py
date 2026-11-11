import gradio as gr
import psutil

def get_system_metrics():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    
    return (
        f"CPU Usage: {cpu_usage}%",
        f"Memory Used: {memory.percent}% ({memory.used // (1024**2)} MB / {memory.total // (1024**2)} MB)",
        f"Disk Free: {disk.free // (1024**3)} GB ({disk.percent}% used)"
    )

demo = gr.Interface(
    fn=get_system_metrics,
    outputs=["text", "text", "text"],
    title="Linux System Telemetry Inspector",
    description="Real-time system health and resource monitoring."
)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860, share=False)