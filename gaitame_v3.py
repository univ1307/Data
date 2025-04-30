import requests

def get_gaitame_signal(pair="USDJPY", long_threshold=60, low_threshold=40):
    """
    Args:
        pair (str): The currency pair to check (default "EURJPY")
        long_threshold (float): Upper threshold for long % (default 60)
        low_threshold (float): Lower threshold for long % (default 40)

    Returns:
        int: 1, -1, or 0 depending on long ratio
    """
    url = "https://navi.gaitame.com/v3/info/tools/position"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()

        for item in data['data']:
            if item['pair'] == pair:
                long_ratio = float(item['ratios'][0]['buy'])
                print(f"{pair} Long: {long_ratio}%")
                if long_ratio >= long_threshold:
                    return -1
                elif long_ratio <= low_threshold:
                    return 1
                else:
                    return 0
        # If pair not found
        print(f"⚠️ {pair} data not found.")
        return 0

    except Exception as e:
        print(f"❌ Error fetching Gaitame data: {e}")
        return 0  # Safe fallback

# Example usage:
if __name__ == "__main__":
    signal = get_gaitame_signal("EURJPY", 60, 49)
    print(f"EURJPY Signal: {signal}")
    signal = get_gaitame_signal()
    print(f"USDJPY Signal: {signal}")