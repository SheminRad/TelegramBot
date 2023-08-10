from telethon import TelegramClient
from constants import api_id
from constants import api_hash

with TelegramClient('anon', api_id, api_hash) as client:
    client.loop.run_until_complete(client.send_message('me', 'Hello, myself!'))