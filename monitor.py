from datetime import datetime

import psutil


OUTPUT_FILE = "/var/www/portfolio/index.html"

CPU_LIMIT = 80
MEMORY_LIMIT = 90
DISK_LIMIT = 85


while True:
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent

    cpu_status = "OK"
    memory_status = "OK"
    disk_status = "OK"

    if cpu >= CPU_LIMIT:
        cpu_status = "WARNING"

    if memory >= MEMORY_LIMIT:
        memory_status = "WARNING"

    if disk >= DISK_LIMIT:
        disk_status = "WARNING"

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    text = (
        f"Simple Server Monitor\n"
        f"Last Update: {now}\n\n"
        f"CPU    : {cpu:.1f}% [{cpu_status}]\n"
        f"Memory : {memory:.1f}% [{memory_status}]\n"
        f"Disk   : {disk:.1f}% [{disk_status}]\n"
    )

    with open(OUTPUT_FILE, "w") as f:
        f.write(text)

    print(
        f"[{now}] CPU: {cpu:.1f}% [{cpu_status}] | "
        f"Memory: {memory:.1f}% [{memory_status}] | "
        f"Disk: {disk:.1f}% [{disk_status}]",
        flush=True,
    )
