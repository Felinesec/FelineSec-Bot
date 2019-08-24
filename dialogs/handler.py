import config
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from utils import util
from . import welcome

def example(bot, update):
	if update.message is not None and update.message.text is not None: 
		if str(update.message.text).lower().startswith("ciao felinesecbot"):
			bot.send_message(update.message.chat_id, text="Ciao {username}"
            .format(username=update.message.from_user.first_name), 
            parse_mode='HTML')

#DICHIARAZIONE FUNZIONI
def init(bot, update):
    example(bot, update)
    util.debug(update)
    welcome.init(bot, update)