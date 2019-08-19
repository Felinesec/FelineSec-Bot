#!/usr/bin/env python3
#   ban.py
#   Python 3.7
#   Version 0.1
#
#   Created by Francesco Masala & @Hersel91
#   Mozilla Public License
#
from admins import decorator


@decorator.restricted
@decorator.cancellacomandi
def init(bot, update):
    pass
    if update.message.text is not None:
        if update.message.text.startswith("/ban"):
            bot.kick_chat_member(update.message.chat_id, update.message.reply_to_message.from_user.id)
