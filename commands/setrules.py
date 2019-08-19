#!/usr/bin/env python3
#   newuser.py
#   Python 3.7
#   Version 0.1
#
#   Created by Talebian & Francesco Masala
#   Mozilla Public License
#

import json
from datetime import datetime
from admins import decorator

@decorator.restricted
def setrules_handler(bot, update):
    user = update.message.from_user
    messagetime = datetime.strftime(datetime.today(), '%H:%M del %d/%m/%Y')

    new_rules = "{}".format(update.message.text[10:])

    rules = {"rules": new_rules }
    with open('commands/felinesec.rules.json', 'w') as rules_js:
        json.dump(rules, rules_js)

    update.message.reply_markdown("*Regole applicate!*")

    # LOG del bot
    user = update.message.from_user
    print('User: {} con ID: {} '.format(user['username'], user['id'])
          + "Ha appena eseguito il seguente comando: /setrules alle ore " + messagetime)
