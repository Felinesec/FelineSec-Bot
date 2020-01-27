#!/usr/bin/env python3
#   setrules.py
#   Python 3.7
#   Version 0.3 "Acrux"
#
#   Created by Talebian & Francesco Masala
#   Mozilla Public License
#
import json
from datetime import datetime
from utils import decorator
from sentry_sdk import capture_message

@decorator.admin.init
def setrules_handler(update, context):
    new_rules = "{}".format(update.message.text[10:])
    rules = {"rules": new_rules }
    with open('commands/felinesec.rules.json', 'w') as rules_js:
        json.dump(rules, rules_js)
    update.message.reply_markdown("*Regole applicate!*")

    # Logging
    user = update.message.from_user
    messagetime = datetime.strftime(datetime.today(), '%H:%M del %d/%m/%Y')
    comando = "setrules"
    capture_message("Un amministratore con ID {} ha appena "
                    .format(user['id']) +
                    "effettuato il comando /" + comando)
    print('Admin: {} con ID: {} '.format(user['username'], user['id'])
          + "Ha appena eseguito il seguente comando: /" + comando +
          " Alle ore " + messagetime)
