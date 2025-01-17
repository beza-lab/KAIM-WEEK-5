from telethon import TelegramClient, events
import asyncio

# telegram credentials
api_id = '27613793'
api_hash = '58f73f500af1aa0f525caff262964fa4'
phone = '+251911756372'
session_name = 'my_session_2'

# Initialize the Telegram client
client = TelegramClient(session_name, api_id, api_hash, use_ipv6=False)

# List of Telegram channels to monitor
channels = ['@Leyueqa', '@ethio_brand_collection', '@Shewabrand']

@client.on(events.NewMessage(chats=channels))
async def handler(event):
    message = event.message.message
    sender_id = event.sender_id
    timestamp = event.date

    if message:
        print(f"Text: {message}")

    if event.message.media:
        await event.message.download_media(file="D:/KAIM/Week 5/KAIM WEEK5")
        print("Media downloaded")

async def main():
    await client.start(phone=phone)
    print("Client started")
    await client.run_until_disconnected()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    if loop.is_running():
        loop.create_task(main())
    else:
        loop.run_until_complete(main())
