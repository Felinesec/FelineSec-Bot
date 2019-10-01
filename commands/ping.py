#!/usr/bin/env python3
#   ping.py
#   Python 3.7
#   Version 0.1
#
#   Created by Francesco Masala & Jack Rendor
#   Mozilla Public License
#
from ping3 import ping
from utils import decorator
from datetime import datetime


@decorator.admin.init
def ping_handler(update, context):
    ms = ping('google.com', unit='ms')
    messagetime = datetime.strftime(datetime.today(), '%H:%M del %d/%m/%Y')
    user = update.message.from_user
    text_markdown0 = "`" + 'Pong!' + "`"
    update.message.reply_markdown(text_markdown0)
    text_markdown1 = "`" + str(ms) + ' ms' + "`"
    update.message.reply_markdown(text_markdown1)
    print('User: {} con ID: {} '.format(user['username'], user['id'])
          + "Ha appena eseguito il seguente comando: /ping alle ore " + messagetime)
