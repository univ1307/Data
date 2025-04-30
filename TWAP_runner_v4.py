# TWAP runner script that accepts arguments for product, direction, size, start/end times, and clips
import sys
import datetime
import time
import random
from trading_ig.rest import IGService
from trading_ig.config import config
from IG_epic import ep, IG_price_multiple, BBG
import Gotobi_alerts as alert
from blotter import blotter_open
import builtins
import os

# Ensure log directory exists
log_dir = "log"
os.makedirs(log_dir, exist_ok=True)

# Open log file inside the log folder
log_path = os.path.join(log_dir, f"twap_runner_log_{datetime.date.today().strftime('%Y%m%d')}.txt")
log_file = open(log_path, "a", encoding="utf-8")

# Override print to log to file and console
def print(*args, **kwargs):
    builtins.print(*args, **kwargs)  # Still prints to terminal
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_file.write(timestamp + " - " + " ".join(str(a) for a in args) + "\n")
    log_file.flush()

# Setup IG connection
def connect():
    global ig_service
    ig_service = IGService(config.username, config.password, config.api_key, config.acc_type)
    ig_service.create_session(None, True)

# Fetch last price and spread from IG
def get_price_and_spread(epic):
    try:
        response = ig_service.fetch_market_by_epic(epic)
        bid = response['snapshot']['bid']
        offer = response['snapshot']['offer']
        mid = (bid + offer) / 2
        spread = abs(offer - bid)
        return mid, spread
    except:
        print(f"Failed to get price for {epic}")
        return 0, 0

# Place IG trade
def ig_trade(ep, size, direction, ccy='GBP', exp='DFB'):
    global trade_count
    if abs(size) >= 500 or trade_count >= trade_count_limit:
        alert.send_email("Trade blocked due to size or limit", ep)
        print(f"Trade blocked: size={size}, trade_count={trade_count}")
        return

    ig_service.create_open_position(
        currency_code=ccy,
        direction='BUY' if direction > 0 else 'SELL',
        epic = ep,
        order_type='MARKET',
        expiry=exp,
        force_open='false',
        guaranteed_stop='false',
        size=abs(size), level=None,
        limit_distance=None,
        limit_level=None,
        quote_id=None,
        stop_level=None,
        stop_distance=None,
        trailing_stop=None,
        trailing_stop_increment=None)
    trade_count += 1

# TWAP entry logic with spread control and retry

def twap_entry(epic, size_per_clip, direction, start_time, end_time, clips, label):
    position = 0
    clips_done = 0
    twap_avg = 0
    gap_time = (end_time - start_time).total_seconds() / clips
    max_spread = 3  # 3 pips
    max_retries = 3

    while clips_done < clips and datetime.datetime.now() < end_time:
        connect()  
        try:
            for attempt in range(max_retries):
                mid, spread = get_price_and_spread(epic)
                print(f"[{label}] Attempt {attempt+1}/{max_retries} - Mid: {mid:.5f}, Spread: {spread:.5f}")

                if mid == 0:
                    print(f"[{label}] Invalid price, skipping attempt.")
                elif spread <= max_spread:
                    ig_trade(epic, size_per_clip, direction)
                    clips_done += 1
                    twap_avg = (twap_avg * position + mid * size_per_clip) / (position + size_per_clip)
                    position += size_per_clip
                    print(f"[{label}] Clip {clips_done}/{clips}, TWAP avg: {twap_avg:.2f}")
                    break
                else:
                    if attempt < max_retries - 1:
                        sleep_time = random.randint(5, 15)
                        print(f"[{label}] Spread too wide ({spread:.5f}). Retrying in {sleep_time}s...")
                        time.sleep(sleep_time)
                    else:
                        print(f"[{label}] Max retries reached. Skipping this clip.")

            time.sleep(gap_time)

        except Exception as e:
            print(f"[{label}] Error during TWAP loop: {e}")

    print(f"[{label}] Done. Final avg: {twap_avg:.2f}, position: {position}")

    # === Square up any leftover ===
    total_size = size_per_clip * clips
    leftover = total_size - position
    if abs(leftover) >= 0.0001:  # Adjust this threshold as needed for practical rounding
        print(f"[{label}] Squaring up remaining size: {leftover:.2f}")
        connect()
        mid, spread = get_price_and_spread(epic)
        #a lot more lenient spread check as we need to sq up
        if mid > 0 and spread <= max_spread * 2:
            ig_trade(epic, leftover, direction)
            twap_avg = (twap_avg * position + mid * leftover) / (position + leftover)
            print(f"[{label}] Final position squared. Updated TWAP avg: {twap_avg:.2f}")
        else:
            print(f"[{label}] Could not square up due to spread or invalid price.")

# Parse CLI args
def parse_args():
    product = sys.argv[1]
    direction = int(sys.argv[2])
    total_size = float(sys.argv[3])
    start_time_str = sys.argv[4]
    end_time_str = sys.argv[5]
    clips = int(sys.argv[6])

    today = datetime.date.today()
    tmr = today + datetime.timedelta(days=1)

    start_dt = datetime.datetime.strptime(f"{today} {start_time_str}", "%Y-%m-%d %H:%M:%S")

    # Try parsing end_dt using today's date first
    end_dt_candidate = datetime.datetime.strptime(f"{today} {end_time_str}", "%Y-%m-%d %H:%M:%S")

    # If end time is earlier than start time, shift end_dt to tomorrow
    if end_dt_candidate <= start_dt:
        end_dt = datetime.datetime.strptime(f"{tmr} {end_time_str}", "%Y-%m-%d %H:%M:%S")
    else:
        end_dt = end_dt_candidate

    return product, direction, total_size, start_dt, end_dt, clips

# === Main Execution ===
trade_count = 0
trade_count_limit = 150

if __name__ == '__main__':

    product, direction, total_size, start_time, end_time, clips = parse_args()
    epic_code = ep(product)
    size_per_clip = round(total_size / clips, 1)

    print(f"Running TWAP: {product}, {direction=}, {total_size=}, {start_time=}, {end_time=}, {clips=}")

    while datetime.datetime.now() < start_time:
        print("Waiting for start time...")
        time.sleep(5)

    twap_entry(epic_code, size_per_clip, direction, start_time, end_time, clips, label=product)
    blotter_open(epic_code, total_size * direction, 0, 0, "")

#30Apr25: v4 can handle end time in NY afternoon 