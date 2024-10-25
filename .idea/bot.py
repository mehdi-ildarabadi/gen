from telethon import TelegramClient

api_id = 'YOUR_API_ID'
api_hash = 'YOUR_API_HASH'

phone = 'YOUR_PHONE_NUMBER'

receiver_username = 'RECEIVER_USERNAME'

message = "Hello, this is a message from my personal account!"

client = TelegramClient('session_name', api_id, api_hash)


async def send_message():
    await client.start(phone)

    await client.send_message(receiver_username, message)

    print("Message sent successfully!")


with client:
    client.loop.run_until_complete(send_message())
