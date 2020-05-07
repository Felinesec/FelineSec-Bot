#!/usr/bin/env python3
#   welcome.py
#   Python 3.7
#   Version 0.3 "Acrux"
#
#   Created by Francesco Masala, Jack Rendor and Hersel Giannella
#   Mozilla Public License
#

import json
from utils import util
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from datetime import datetime

def init(update, context):
    with open('commands/felinesec.rules.json') as f:
        data = json.load(f)

    rules = data['rules']
    button_list = [InlineKeyboardButton("Regole", callback_data="rules"),
                   InlineKeyboardButton("Gruppo OT", url="https://t.me/FelineSecOT"),
                   InlineKeyboardButton("Sito", url="https://felinesec.com"),
                   InlineKeyboardButton("Forum", url="https://forum.felinesec.com")]
    reply_markup = InlineKeyboardMarkup(util.build_menu(button_list, n_cols=2))

    for new in update.message.new_chat_members:
        update.message.reply_markdown('Benvenuto {username} _({user_id})_ su {group}, premi su Regole per'
                                      ' _leggere le regole_'
                                      ', premi su OT per raggiungere _il gruppo OT_, per Sito '
                                      'e Forum premi i corrispettivi pulsanti.'.format(
                                                         username="@"+new.username,
                                                         user_id=update.message.from_user.id,
                                                         group=update.message.chat.title), reply_markup=reply_markup)


def newuser_handler(bot, update):
    newuser(bot, update)

    messagetime = datetime.strftime(datetime.today(), '%H:%M del %d/%m/%Y')
    print('Il seguente utente {username} \u00e8 appena entrato nel gruppo {gruppo} alle {orario}'
          .format(username=update.message.from_user.first_name,
                  gruppo=update.message.chat.title,
                  orario=messagetime))
