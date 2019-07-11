#!/usr/bin/env python3
#   newuser.py
#   Python 3.7
#   Version 0.1
#
#   Created by Francesco Masala & Jack Rendor
#   Mozilla Public License
#
import config


def newuser(bot, update):
    for new in update.message.new_chat_members:
        update.message.reply_text('Benvenuto {username} in {chat_title}'
                                  .format(username=update.message.from_user.first_name,
                                          chat_title=update.message.chat.title))


def init(bot, update):
    newuser(bot, update)
