#!/usr/bin/env python3
#   start.py
#   Python 3.7
#   Version 0.1
#
#   Created by Francesco Masala & Jack Rendor
#   Mozilla Public License
#
from datetime import datetime
import config


def start_handler(bot, update):
    text = (
        "Benvenuto!\nEcco qua una lista dei comandi disponibili:\n"
        "/server\n"
        "Per altre informazioni fai /help"
    )
    update.message.reply_text(text)
    user = update.message.from_user
    messagetime = datetime.strftime(datetime.today(), '%H:%M del %d/%m/%Y')
    print('User: {} con ID: {} '.format(user['username'], user['id'])
          + "Ha appena eseguito il seguente comando: /start alle ore " + messagetime)
