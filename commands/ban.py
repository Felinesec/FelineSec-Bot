#!/usr/bin/env python3
#   ban.py
#   Python 3.7
#   Version 0.3 "Acrux"
#
#   Created by Francesco Masala and Hersel Giannella
#   Mozilla Public License
#
from utils import decorator


@decorator.admin.init
@decorator.delete.init
def ban_handler(update, context):
    user = update.message.from_user
    text = ('User: {} con ID: {} '.format(user['username'], user['id'])
          + "E' stato bannato con successo ")
    update.message.reply_text(text)
    user = update.message.from_user
    bot.kick_chat_member(update.message.chat_id, update.message.reply_to_message.from_user.id)
