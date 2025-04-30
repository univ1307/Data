# Script to launch multiple TWAP runs using subprocess and accept sizes + clips via CLI
import subprocess
import datetime
import time
import sys

import builtins
import os

# Ensure log directory exists
log_dir = "log"
os.makedirs(log_dir, exist_ok=True)

# Open log file inside the log folder
log_path = os.path.join(log_dir, f"twap_launcher_log_{datetime.date.today().strftime('%Y%m%d')}.txt")
log_file = open(log_path, "a", encoding="utf-8")

# Override print to log to file and console
def print(*args, **kwargs):
    builtins.print(*args, **kwargs)  # Still prints to terminal
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_file.write(timestamp + " - " + " ".join(str(a) for a in args) + "\n")
    log_file.flush()

# # Get external arguments: total_size1, total_size2, clips
# try:
#     total_size1 = float(sys.argv[1])  # For JPY
#     total_size2 = float(sys.argv[2])  # For EURJPY
#     clips = int(sys.argv[3])
# except Exception as e:
#     print("Usage: python twap_launcher.py <total_size1> <total_size2> <clips>")
#     sys.exit(1)

# Define TWAP tasks
jobs = [
    {
        'product': 'EUR',
        'direction': '-1',
        'total_size': '100',
        'start_time': '21:30:28',
        'end_time': '22:29:58',
        'clips': '20'
    },
    {
        'product': 'EUR',
        'direction': '1',
        'total_size': '200',
        'start_time': '22:55:08',
        'end_time': '23:00:00',
        'clips': '20'
    },
    {
        'product': 'EUR',
        'direction': '-1',
        'total_size': '100',
        'start_time': '23:30:08',
        'end_time': '00:30:00',
        'clips': '20'
    }
]

# Launch each job as a subprocess
for job in jobs:
    args = [
        'python', 'TWAP_runner_v4.py',
        job['product'],
        str(job['direction']),
        str(job['total_size']),
        job['start_time'],
        job['end_time'],
        str(job['clips'])
    ]
    print("Launching:", ' '.join(args))
    subprocess.Popen(args)
    time.sleep(1)  # slight delay to stagger launches