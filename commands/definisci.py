#!/usr/bin/env python3
#   definisci.py
#   Python 3.7
#   Version 0.1
#
#   Created by Talebian , Modified by Hersel Giannella
#   Mozilla Public License
#


import wikipedia as wiki
from datetime import datetime
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from utils import util


def definisci_handler(update, context):
    bot = context.bot
    arg = update.message.text[5:]
    wiki.set_lang('it')
    try:
        pg = wiki.page(wiki.search(arg)[0])
        title = pg.title
        pg_url = pg.url
        definizione = pg.summary
        button_list = [InlineKeyboardButton("View on Wikipedia", url=pg_url)]
        reply_markup = InlineKeyboardMarkup(util.build_menu(button_list, n_cols=1))
        text = "*{}:*\n\n{}".format(title, definizione)
        update.message.reply_markdown(text, reply_markup=reply_markup)
    except:
        bot.send_message(update.message.chat_id, text="Mi spiace {user} non ho trovato quello che cercavi"
                         .format(user=update.message.from_user.first_name))
    # LOG del bot
    user = update.message.from_user
    messagetime = datetime.strftime(datetime.today(), '%H:%M del %d/%m/%Y')
    print('User: {} con ID: {} '.format(user['username'], user['id'])
          + "Ha appena eseguito il seguente comando: /wiki alle ore " + messagetime)
