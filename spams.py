from time import sleep
from pyrogram import Client, filters, types
from PIL import Image
import re
import asyncio

app = Client('session', api_id=, api_hash='') # после ровно в api_id и api_hash подставляем свои данные с https://my.telegram.org/auth

chat_id = "@aanonchatbot" #Сюда айди чата

@app.on_message(chat_id)
async def spam(client: Client, message: types.Message):
    if "Ты нашел себе собеседника" in message.text: # Меняем это значение если хотим спамить в другом чате
        sleep(1) # Это задержки между сообщениями
        await app.send_message(chat_id,"приветик")
        sleep(1.3)
        await app.send_message(chat_id,"Д")
        sleep(2)
        await app.send_message(chat_id,"Если хочешь узнать что такое истенная красота то кликай на стикер👇🏼🔞")
        await app.send_sticker(chat_id,"CAACAgIAAxkBAAIcimPblquKPR3Wo4N6GuUHnYoC7_cZAAI0KAACiq_hSqIScPV7MMGbLgQ") # В кавычки айди стикера которое берем тут @idstickerbot
        sleep(1) # Это задержки между сообщениями 
        await app.send_message(chat_id,"/stop")
        sleep(2)
        await app.send_message(chat_id,"🎲Случайный собеседник")

app.run() # Что бы начать спам просто начнаем поиск в чате где хотим спамить

#Spamer by anon_chats from FARUM
