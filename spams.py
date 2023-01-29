from time import sleep
from pyrogram import Client, filters, types
from PIL import Image
import re
import asyncio

app = Client('session', api_id=, api_hash='') # после ровно в api_id и api_hash подставляем свои данные с https://my.telegram.org/auth

chat_id = "@AnonRuBot" #Сюда айди чата

# В папке с этим файлом создаем файл "text.txt" и в него пишем текст которым хотим спамить
file1 = "text.txt"
with open (file1, 'r') as file:
    text = file.read()

@app.on_message(chat_id)
async def spam(client: Client, message: types.Message):
    if "Собеседник найден 😺" in message.text: # Меняем это значение если хотим спамить в другом чате
        sleep(2) # Это задержки между сообщениями
        #await app.send_message(chat_id,text) # Если хотите спамить текстом то уберите решетку в начале и поставьте ее перед след строкой
        await app.send_sticker(chat_id,"CAACAgIAAxkBAAEHabtjz9yi9SCOxWiI0WB5-KUxs5ARVQAC5ygAAlqzgUrc1w118xlZ8y0E") # В кавычки айди стикера которое берем тут @idstickerbot
        sleep(2) # Это задержки между сообщениями 
        
        if "Собеседник найден 😺" in message.text: # Меняем это значение если хотим спамить в другом чате
            await app.send_message(chat_id,"/next")
    
    if "Собеседник закончил с вами связь 😞" in message.text: # Меняем это значение если хотим спамить в другом чате
        await app.send_message(chat_id,"/next")

    if "Вы закончили связь с вашим собеседником 🙄" in message.text: # Меняем это значение если хотим спамить в другом чате
        await app.send_message(chat_id,"/next")

app.run() # Что бы начать спам просто начнаем поиск в чате где хотим спамить

#Spamer by anon_chats from FARUM
