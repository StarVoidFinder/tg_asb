import telebot
import config

bot = telebot.TeleBot(config.token)

#print(config.token)
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")


bot.polling()