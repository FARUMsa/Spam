from time import sleep
from pyrogram import Client, filters, types
from PIL import Image
import re
import asyncio

app = Client('session', api_id=9470354, api_hash='09583bf3a3bf5f4824fb68faa8f61dad')

chat_id = "@AnonRuBot"

file1 = "text.txt"
with open (file1, 'r') as file:
    text = file.read()

@app.on_message(chat_id)
async def spam(client: Client, message: types.Message):
    if "Собеседник найден 😺" in message.text:
        #await app.send_message(chat_id,text)
        await app.send_sticker(chat_id,"CAACAgIAAxkBAAEHabtjz9yi9SCOxWiI0WB5-KUxs5ARVQAC5ygAAlqzgUrc1w118xlZ8y0E")
        sleep(2)
        await app.send_message(chat_id,"/stop")
        sleep(1)
        await app.send_message(chat_id,"🚀 Поиск любого собеседника")
app.run()