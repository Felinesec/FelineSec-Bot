#!/usr/bin/env python3
#   help.py
#   Python 3.7
#   Version 0.1
#
#   Created by Francesco Masala & Jack Rendor
#   Mozilla Public License
#
from datetime import datetime


def help_handler(bot, update):
    text=(
        "*/server*: Indica le principali statistiche del server _(Uptime, utilizzo della cpu e della ram)_\n"
        "*/wiki {arg}*: cerca la definizione su wikipedia\n"
        "*/setrules {arg}*: imposta le regole\n"
        "*/rules {arg}*:vedi le regole\n"
        "*/help*: mostra questa guida"
    )
    update.message.reply_markdown(text)
    user = update.message.from_user
    messagetime = datetime.strftime(datetime.today(), '%H:%M %d/%m/%Y')
    print('User: {} con ID: {} '.format(user['username'], user[
        'id']) + "Ha appena eseguito il seguente comando: /help alle ore " + messagetime)
