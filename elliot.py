import telebot # Libreria de la API del bot
from telebot import types # Tipos para la API del bot 
import time 
import telegram
from telegram.ext import *

ElliotMr_bot = telegram.Bot(token="561130598:AAFmqjgBeRFK2SAY5RjmEjXXMyEUGKvk2vI")
ElliotMr_bot_updater = Updater(ElliotMr_bot.token)

def listener(bot,update):
	id = update.messege.chat_id
	mensaje = update.messege.text
	print("ID: "+str(id) + " MENSAJE: " + mensaje)

def start(bot, update, pass_chat_data = True):
	update.messege.chat_id
	bot.sendMessage(chat_id=update.messege.chat_id, text = "Gracias por usarme!")

start_handler = CommandHandler('start', start)
listener_handler = MessageHandler(Filters.text, listener)

dispatcher = ElliotMr_bot_updater.dispatcher

dispatcher.add_handler(start_handler)
dispatcher.add_handler(listener_handler)

ElliotMr_bot_updater.start_polling()
ElliotMr_bot_updater.idle()

while True:
	pass