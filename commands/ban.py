#!/usr/bin/env python3
#   ban.py
#   Python 3.7
#   Version 0.1
#
#   Created by Francesco Masala
#   Mozilla Public License
#
from admins import decorator


@decorator.restricted
@decorator.cancellacomandi
def ban_handler(bot, update):
    user = update.message.from_user
    text = ('User: {} con ID: {} '.format(user['username'], user['id'])
          + "E' stato bannato con successo ")
    update.message.reply_text(text)
    user = update.message.from_user
    bot.kick_chat_member(update.message.chat_id, update.message.reply_to_message.from_user.id)
