from telegram.ext import Updater, CommandHandler
import requests
import re

def get_url():
	contents = requests.get("https://random.dog/woof.json").json()
	url = contents['url']
	return url

def pic(bot, update):
	url = get_url()
	chat_id = update.messages.chat_id
	bot.send_photo(chat_id = chat_id, photo = url)

def main():
	updater = Updater("731370184:AAFwaddEXzRtOcTNI07XtTzIYaIUcppiYYI")
	dp = updater.dispatcher
	dp.add_handler(CommandHandler('pic', pic))
	updater.start_polling()
	updater.idle()

if __name__ == "__main__":
	main()
