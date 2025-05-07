# use flow intel to trade automatically
import subprocess
import datetime
import time
import math
from TWAP_runner_v5 import get_price_and_spread, connect
from IG_epic import ep
from sizing import sizing
import builtins
import os

VAR = 200 #fear and greed, be extra careful of that

# Ensure log directory exists
log_dir = "log"
os.makedirs(log_dir, exist_ok=True)

# Open log file inside the log folder
log_path = os.path.join(log_dir, f"flow_intel_launcher_log_{datetime.date.today().strftime('%Y%m%d')}.log")
log_file = open(log_path, "a", encoding="utf-8")

# Override print to log to file and console
def print(*args, **kwargs):
    builtins.print(*args, **kwargs)  # Still prints to terminal
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_file.write(timestamp + " - " + " ".join(str(a) for a in args) + "\n")
    log_file.flush()

# Step 1: Get Flow Intel. Automate later
###############################################
intel_source = "EQ, YSL"
product = "NQA" 
direction = "1"
implied_vol = 25
clips = 1
###############################################
connect()
last, spread = get_price_and_spread(ep(product)) 

# Step 2: Determine size and other details. Automate later
entry_date = "2025-05-07"
entry_start_time = "20:08:55"
entry_end_time = "20:09:00"
exit_date = "2025-05-08"
exit_start_time = "07:59:00"
exit_end_time = "08:00:00"

entry_start = datetime.datetime.strptime(f"{entry_date} {entry_start_time}", "%Y-%m-%d %H:%M:%S")
entry_end = datetime.datetime.strptime(f"{entry_date} {entry_end_time}", "%Y-%m-%d %H:%M:%S")
exit_start = datetime.datetime.strptime(f"{exit_date} {exit_start_time}", "%Y-%m-%d %H:%M:%S")
exit_end = datetime.datetime.strptime(f"{exit_date} {exit_end_time}", "%Y-%m-%d %H:%M:%S")

# Adjust if end is earlier (i.e. crosses midnight)
if entry_end <= entry_start:
    entry_end += datetime.timedelta(days=1)
if exit_end <= exit_start:
    exit_end += datetime.timedelta(days=1)

days_run = (exit_start.date() - entry_start.date()).days
total_size = round(sizing(last, implied_vol, max(days_run,1), VAR),2)
exit_direction = str(-1 * int(direction))

# Step 3: Execution, recording
# Define TWAP tasks
jobs = [
    {
        'product': product,
        'direction': direction,
        'total_size': total_size,
        'start_time': entry_start,
        'end_time': entry_end,
        'clips': str(clips)
    },
    {
        'product': product,
        'direction': exit_direction,
        'total_size': total_size,
        'start_time': exit_start,
        'end_time': exit_end,
        'clips': str(clips)
    }
]

# Launch each job as a subprocess
for job in jobs:
    args = [
        'python', 'TWAP_runner_v5_fulldate.py',
        job['product'],
        str(job['direction']),
        str(job['total_size']),
        job['start_time'].strftime("%Y-%m-%d %H:%M:%S"),
        job['end_time'].strftime("%Y-%m-%d %H:%M:%S"),
        str(job['clips']),
        intel_source
    ]
    print("Launching:", ' '.join(args))
    subprocess.Popen(args)
    time.sleep(1)  # slight delay to stagger launches