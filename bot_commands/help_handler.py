#!/usr/bin/env python3
#   example.config.py
#   Python 3.7
#   Version 0.1
#
#   Created by Francesco Masala & Jack Rendor
#   Mozilla Public License
#
def help_handler(bot, update):
    text="/server = Indica le principali statistiche del server (Uptime, utilizzo della cpu e della ram)"
    update.message.reply_text(text)
    user = update.message.from_user
    messagetime = datetime.strftime(datetime.today(), '%H:%M %d/%m/%Y')
    print('User: {} con ID: {} '.format(user['username'], user[
        'id']) + "Ha appena eseguito il seguente comando: /help alle ore " + messagetime)