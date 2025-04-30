from gaitame_v3 import get_gaitame_signal

#goal is to determine early entry or not
#enjoy some beta in trending market
def scrap_data():
    global early_entry_flag, late_exit_flag
    gaitame_signal = get_gaitame_signal()
    if gaitame_signal > 0:
        early_entry_flag = '1'
        late_exit_flag = '0'
    elif gaitame_signal < 0:
        late_exit_flag = '1'
        early_entry_flag = '0'
    else:
        early_entry_flag = '0'
        late_exit_flag = '0'
    print(f"gaitame_signal: {gaitame_signal}; early_entry_flag: {early_entry_flag}; late_exit_flag: {late_exit_flag}")

def get_late_exit_flag():
    scrap_data()
    return late_exit_flag

def get_early_entry_flag():
    scrap_data()
    return early_entry_flag

# gaitame_eurjpy_signal = get_gaitame_signal("EURJPY",60,49)
# if gaitame_eurjpy_signal > 0:
#     late_exit_flag = '1'
# else:
#     early_entry_flag = '0'

# print(f"gaitame_signal: {gaitame_signal}; early_entry_flag: {early_entry_flag}")

# Example usage:
if __name__ == "__main__":
    print(f"Early Entry Flag: {get_early_entry_flag()}")
    print(f"Late Exit Flag: {get_late_exit_flag()}")
