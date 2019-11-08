#!/usr/bin/env python3
#   server.py
#   Python 3.7
#   Version 0.3 "Acrux"
#
#   Created by Francesco Masala & Jack Rendor
#   Mozilla Public License
#
from time import time
from datetime import timedelta, datetime
from psutil import cpu_percent, virtual_memory, boot_time
from utils import decorator


@decorator.admin.init
def server_handler(update, context):
    messagetime = datetime.strftime(datetime.today(), '%H:%M del %d/%m/%Y')
    user = update.message.from_user
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
