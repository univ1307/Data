import requests

# === CONFIG ===
repo_owner = "univ1307"
repo_name = "Data"
file_path = "gaitame.json"
save_as = "gaitame.json"

# === DOWNLOAD ===
url = f"https://raw.githubusercontent.com/{repo_owner}/{repo_name}/main/{file_path}"

response = requests.get(url)
if response.status_code == 200:
    with open(save_as, 'wb') as f:
        f.write(response.content)
    print(f"✅ Downloaded and saved as {save_as}")
else:
    print(f"❌ Failed to download. Status code: {response.status_code}")
