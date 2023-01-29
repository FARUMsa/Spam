from time import sleep
from pyrogram import Client, filters, types
from PIL import Image
import re
import asyncio

app = Client('session', api_id=9470354, api_hash='09583bf3a3bf5f4824fb68faa8f61dad') #вместо api_id и api_hash подставляем свои данные с https://my.telegram.org/auth

chat_id = "@AnonRuBot" #Сюда айди чата

@app.on_message(chat_id)
async def spam(client: Client, message: types.Message):
    if "Собеседник найден 😺" in message.text:
        sleep(2) #Это задержки между сообщениями 
        await app.send_sticker(chat_id,"CAACAgIAAxkBAAEHabtjz9yi9SCOxWiI0WB5-KUxs5ARVQAC5ygAAlqzgUrc1w118xlZ8y0E") #В кавычки айди стикера которое берем тут @idstickerbot
        sleep(2) #Это задержки между сообщениями 
        if "Собеседник найден 😺" in message.text:
            await app.send_message(chat_id,"/stop")
            sleep(1) #Это задержки между сообщениями 
            await app.send_message(chat_id,"🚀 Поиск любого собеседника")
    if "Собеседник закончил с вами связь 😞" in message.text:
        await app.send_message(chat_id,"🚀 Поиск любого собеседника")

app.run()

#Spamer by anon_chats by FARUM
