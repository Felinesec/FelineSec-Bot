#   admin.py
#   Python 3.7
#   Version 0.1
#
#   Created by Francesco Masala and Hersel Giannella
#   Mozilla Public License
#
import config
from functools import wraps

def init(func):
    @wraps(func)
    def wrapped(update, context):
        user_id = update.effective_user.id
        if user_id not in config.LIST_OF_ADMINS:
            print("Unauthorized access denied for {}.".format(user_id))
            return
        return func(update, context)
    return wrapped
