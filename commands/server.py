#   server.py
#   Python 3.7
#   Version 0.1
#
#   Created by Francesco Masala & Jack Rendor
#   Mozilla Public License
#
import config
from time import time
from datetime import timedelta, datetime
from psutil import cpu_percent, virtual_memory, boot_time

def server_handler(bot, update):
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
    text = (
        "Ecco qua le statistiche del server:\n\n"
        "CPU: " + str(cpu_percent())+"%\n"
        "RAM: " + str(virtual_memory().percent)+"%\n"
        "Uptime: " + str(
            timedelta(
                seconds=(time() - boot_time())
            )
        )+"\n"
        "Boot time: " + str(
            datetime.fromtimestamp(
                boot_time()
            ).strftime("%Y-%m-%d %H:%M:%S")
        )
    )

    text_markdown = "`" + text + "`"
    update.message.reply_markdown(text_markdown)
    print('User: {} con ID: {} '.format(user['username'], user['id'])
          + "Ha appena eseguito il seguente comando: /server alle ore " + messagetime)
