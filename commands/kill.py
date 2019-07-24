#   server.py
#   Python 3.7
#   Version 0.1
#
#   Created by Francesco Masala & Jack Rendor
#   Mozilla Public License
#
import config
from datetime import datetime
import os


def kill_handler(bot, update):
    messagetime = datetime.strftime(datetime.today(), '%H:%M del %d/%m/%Y')
    user = update.message.from_user
    if not update.message.from_user.id in config.admin_list:
        sudoers=("User not in the sudoers list.")
        sudoers_markdown = "`" + sudoers + "`"
        update.message.reply_markdown(sudoers_markdown)
        print('User: {} con ID: {} '.format(user['username'], user['id'])
              + "Ha provato ed eseguire il comando /server alle ore: " + messagetime
              + "\n La sua richiesta \u00e8 stata rifiutata poich\u00e8 esso non rientra nella lista sudoers"
              )
        return
    text = ('Il bot \u00e8 stato terminato')
    text_markdown = "`" + text + "`"
    update.message.reply_markdown(text_markdown)
    print('User: {} con ID: {} '.format(user['username'], user['id'])
          + "Ha appena eseguito il seguente comando: /server alle ore " + messagetime)
    os.kill(os.getpid(), 9)
