#   admin.py
#   Python 3.7
#   Version 0.3 "Acrux"
#
#   Created by Francesco Masala and Hersel Giannella
#   Mozilla Public License
#
import config
from functools import wraps
from sentry_sdk import capture_message


def init(func):
    @wraps(func)
    def wrapped(update, context):
        if update.effective_user is not None:
            user_id = update.effective_user.id
            if user_id not in config.LIST_OF_ADMINS:
                capture_message("L'utente con ID {} ha"
                                " provato ad usare un comando riservato"
                                " ad un founder.".format(user_id))
                text_markdown = "`" + "Unauthorized access denied for {}.".format(user_id) + "`"
                update.message.reply_markdown(text_markdown)
                print("Unauthorized access denied for {}.".format(user_id))
                return
        else:
            return
        return func(update, context)
    return wrapped
