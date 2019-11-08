#!/usr/bin/env python3
#   kill.py
#   Python 3.7
#   Version 0.3 "Acrux"
#
#   Created by Francesco Masala & Jack Rendor
#   Mozilla Public License
#
import config
from datetime import datetime
import os
from utils import decorator

@decorator.owner.init
def kill_handler(update, context):
    messagetime = datetime.strftime(datetime.today(), '%H:%M del %d/%m/%Y')
    user = update.message.from_user
    text = ('Il bot \u00e8 stato terminato')
    text_markdown = "`" + text + "`"
    update.message.reply_markdown(text_markdown)
    print('User: {} con ID: {} '.format(user['username'], user['id'])
          + "Ha appena eseguito il seguente comando: /server alle ore " + messagetime)
    os.kill(os.getpid(), 9)
