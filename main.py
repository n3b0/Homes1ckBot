
import os
import telebot


my_secret = os.environ['API-KEY']
bot = telebot.TeleBot('API-KEY')


@bot.message_handler(commands=['Hello'])
def send_welcome(message):
  bot.reply_to(message, "Hey! how are you?")

  bot.polling()



  