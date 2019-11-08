#   owner.py
#   Python 3.7
#   Version 0.3 "Acrux"
#
#   Created by Francesco Masala and Hersel Giannella
#   Mozilla Public License
#
import config
from functools import wraps
#OWNERBOT


def init(func):
    @wraps(func)
    def wrapped(update, context):

        if update.effective_user is not None:
            user_id = update.effective_user.id
            if user_id not in config.OWNER_LIST:
                print("Unauthorized access denied for {}.".format(user_id))
                return
        else:
            return False
        return func(update, context)
    return wrapped
