#   delete.py
#   Python 3.7
#   Version 0.1
#
#   Created by Francesco Masala and Hersel Giannella
#   Mozilla Public License
#
from functools import wraps
#DELETE COMMAND
def init(func):
    @wraps(func)
    def wrapped(update, context):
        bot = context.bot
        if update.message.text is not None:
          if update.message.text.startswith("/"):
              bot.delete_message(update.message.chat_id, update.message.message_id)
        return func(update, context)
    return wrapped
