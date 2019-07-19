#!/usr/bin/env python3
#   newuser.py
#   Python 3.7
#   Version 0.1
#
#   Created by Talebian
#   Mozilla Public License
#


import wikipedia as wiki
from datetime import datetime
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from build_menu import build_menu


def definisci_handler(bot, update):
    
    # Recupero della definizione
    arg = update.message.text[5:]
    wiki.set_lang('it')
    pg = wiki.page(wiki.search(arg)[0])
    title = pg.title
    pg_url = pg.url
    definizione = pg.summary

    button_list = [InlineKeyboardButton("View on Wikipedia", url=pg_url)]
    
    reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=1))

    text = "*{}:*\n\n{}".format(title, definizione)

    # Risposta del Bot
    update.message.reply_markdown(text, reply_markup=reply_markup)
    
    # LOG del bot
    user = update.message.from_user
    messagetime = datetime.strftime(datetime.today(), '%H:%M del %d/%m/%Y')
    print('User: {} con ID: {} '.format(user['username'], user['id'])
          + "Ha appena eseguito il seguente comando: /wiki alle ore " + messagetime)
    

