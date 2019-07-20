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
import config


def setrules_handler(bot, update):
    user = update.message.from_user
    messagetime = datetime.strftime(datetime.today(), '%H:%M del %d/%m/%Y')
    if not update.message.from_user.id in config.admin_list:
        sudoers=("User not in the sudoers list.")
        sudoers_markdown = "`" + sudoers + "`"
        update.message.reply_markdown(sudoers_markdown)
        print('User: {} con ID: {} '.format(user['username'], user['id'])
              + "Ha provato ed eseguire il comando /setrules alle ore: " + messagetime
              + "\n La sua richiesta \u00e8 stata rifiutata poich\u00e8 esso non rientra nella lista sudoers"
              )
        return

    new_rules = "{}".format(update.message.text[10:])

    rules = {"rules": new_rules }
    with open('commands/felinesec.rules.json', 'w') as rules_js:
        json.dump(rules, rules_js)

    update.message.reply_markdown("*Regole applicate!*")

    # LOG del bot
    user = update.message.from_user
    print('User: {} con ID: {} '.format(user['username'], user['id'])
          + "Ha appena eseguito il seguente comando: /setrules alle ore " + messagetime)
