#!/usr/bin/env python3
#   newuser.py
#   Python 3.7
#   Version 0.1
#
#   Created by Talebian
#   Mozilla Public License
#

import json
from datetime import datetime


def rules_handler(bot, update):
    with open('commands/felinesec.rules.json') as rules_js:
        data = json.load(rules_js)

    rules = "*Regole:*\n\n{rules}".format(rules=data['rules'])

    update.message.reply_markdown(rules)

# LOG del bot
    user = update.message.from_user
    messagetime = datetime.strftime(datetime.today(), '%H:%M del %d/%m/%Y')
    print('User: {} con ID: {} '.format(user['username'], user['id'])
          + "Ha appena eseguito il seguente comando: /rules alle ore " + messagetime)
