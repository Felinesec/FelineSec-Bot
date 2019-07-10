#!/usr/bin/env python3
#   example.config.py
#   Python 3.7
#   Version 0.1
#
#   Created by Francesco Masala & Jack Rendor
#   Mozilla Public License
#
def server_handler(bot, update):
    # if update.message.from_user.id in admin_list:
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
    update.message.reply_text(text)
    user = update.message.from_user
    messagetime = datetime.strftime(datetime.today(), '%H:%M del %d/%m/%Y')
    print('User: {} con ID: {} '.format(user['username'], user['id'])
          + "Ha appena eseguito il seguente comando: /server alle ore " + messagetime)