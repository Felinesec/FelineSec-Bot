#!/usr/bin/env python3
#   help.py
#   Python 3.7
#   Version 0.3 "Acrux"
#
#   Created by Francesco Masala & Jack Rendor
#   Mozilla Public License
#
from datetime import datetime
from sentry_sdk import capture_message


def help_handler(update, context):
    text=(
        "*/server*: Indica le principali statistiche del server _(Uptime, utilizzo della cpu e della ram)_\n"
        "*/wiki {arg}*: cerca la definizione su wikipedia\n"
        "*/setrules {arg}*: imposta le regole\n"
        "*/rules {arg}*:vedi le regole\n"
        "*/help*: mostra questa guida\n"
        "*/ping*: effetua un ping su *google.com*\n"
    )
    update.message.reply_markdown(text)
    user = update.message.from_user
    messagetime = datetime.strftime(datetime.today(), '%H:%M del %d/%m/%Y')
    comando = "help"
    capture_message("Un utente con ID {} ha appena "
                    .format(user['id']) +
                    "effettuato il comando /" + comando)
    print('User: {} con ID: {} '.format(user['username'], user['id'])
          + "Ha appena eseguito il seguente comando: /" + comando +
          " Alle ore " + messagetime)
