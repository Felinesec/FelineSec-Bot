#!/usr/bin/env python3
#   ping.py
#   Python 3.7
#   Version 0.3 "Acrux"
#
#   Created by Francesco Masala & Jack Rendor
#   Mozilla Public License
#
from ping3 import ping
from utils import decorator
from datetime import datetime
from sentry_sdk import capture_message


@decorator.admin.init
def ping_handler(update, context):
    ms = ping('google.com', unit='ms')
    text_markdown0 = "`" + 'Pong!' + "`"
    update.message.reply_markdown(text_markdown0)
    text_markdown1 = "`" + str(ms) + ' ms' + "`"
    update.message.reply_markdown(text_markdown1)

    # Logging
    user = update.message.from_user
    messagetime = datetime.strftime(datetime.today(), '%H:%M del %d/%m/%Y')
    comando = "ping"
    capture_message("Un admin con ID {} ha appena "
                    .format(user['id']) +
                    "effettuato il comando /" + comando)
    print('Admin: {} con ID: {} '.format(user['username'], user['id'])
          + "Ha appena eseguito il seguente comando: /" + comando +
          " Alle ore " + messagetime)
