#!/usr/bin/env python3
#   newuser.py
#   Python 3.7
#   Version 0.1
#
#   Created by Francesco Masala & Jack Rendor
#   Mozilla Public License
#
from datetime import datetime


def newuser(bot, update):
    for new in update.message.new_chat_members:
        update.message.reply_text('Benvenuto {username} in {gruppo}'
                                  .format(username=update.message.from_user.first_name,
                                          gruppo=update.message.chat.title))


def newuser_handler(bot, update):
    newuser(bot, update)
    messagetime = datetime.strftime(datetime.today(), '%H:%M del %d/%m/%Y')
    print('Il seguente utente {username} e appena entrato nel gruppo {gruppo}'
          .format(username=update.message.from_user.first_name,
                  gruppo=update.message.chat.title))  # todo accento
