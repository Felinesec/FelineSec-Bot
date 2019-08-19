#!/usr/bin/env python3
#   newuser.py
#   Python 3.7
#   Version 0.1
#
#   Created by @Hersel91 and modified by Francesco Masala
#   Mozilla Public License
#

import json
from datetime import datetime

from functools import wraps


LIST_OF_ADMINS = [44222507, 33003926, 358176315, 866272007]

def restricted(func):
    @wraps(func)
    def wrapped(bot, update):
        user_id = update.effective_user.id
        if user_id not in LIST_OF_ADMINS:
            print("Unauthorized access denied for {}.".format(user_id))
            text_markdown = "`" + 'Utente non riconosciuto' + "`"
            update.message.reply_markdown(text_markdown)
            return
        return func(bot, update)
    return wrapped

#CANCELLA COMANDI
def cancellacomandi(func):
    @wraps(func)
    def wrapped(bot, update):
        if update.message.text is not None:
          if update.message.text.startswith("/"):
            bot.delete_message(update.message.chat_id, update.message.message_id)
        return func(bot, update)
    return wrapped
#OWNERBOT
OWNER_LIST= [44222507, 33003926]

def ownerbot(func):
    @wraps(func)
    def wrapped(bot, update):
        user_id = update.effective_user.id
        if user_id not in OWNER_LIST:
            print("Unauthorized access denied for {}.".format(user_id))
            text_markdown = "`" + 'Utente non riconosciuto' + "`"
            update.message.reply_markdown(text_markdown)
            return
        return func(bot, update)
    return wrapped
