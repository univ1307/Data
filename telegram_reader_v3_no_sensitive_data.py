from telethon import TelegramClient, events

# Fill in your credentials
api_id = 1        # e.g. 1234567
api_hash = ''      # e.g. 'a1b2c3d4...'
session_name = 'SBNet_reader'

# Create the client
client = TelegramClient(session_name, api_id, api_hash)

@client.on(events.NewMessage)
async def handler(event):
    message = event.raw_text
    if "#SBNet" in message:
        payload = message.split("#SBNet", 1)[1].strip()
        try:
            import json
            data = json.loads(payload)
            print("Parsed JSON:", data)
        except:
            try:
                value = float(payload)
                print("Parsed number:", value)
            except:
                print("Raw text:", payload)

# Start the client
client.start()
print("Listening for #SBNet messages...")
client.run_until_disconnected()
