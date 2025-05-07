#utility: calculate size
import math

def sizing(last, implied_vol, days_run, var):
    expected_move_in_pct = implied_vol / math.sqrt(252) * math.sqrt(days_run)
    if last == 0:
        print("Warning, last is 0. Possible problems with feed")
        return 0
    else:
        return (var / (expected_move_in_pct) * 100 / last)
