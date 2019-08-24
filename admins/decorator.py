#!/usr/bin/env python3
#   decorator.py
#   Python 3.7
#   Version 0.1
#
#   Created by @Hersel91 and modified by Francesco Masala
#   Mozilla Public License
#
from functools import wraps


LIST_OF_ADMINS = [44222507, 33003926, 358176315, 866272007]

def restricted(func):
    @wraps(func)
    def wrapped(bot, update):
        user_id = update.effective_user.id
        if user_id not in LIST_OF_ADMINS:
            print("Unauthorized access denied for {}.".format(user_id))
            text_markdown = "`" + 'Utente non riconosciuto' + "`"
            update.message.reply_markdown(text_markdown)
            return
        return func(bot, update)
    return wrapped

#CANCELLA COMANDI
def cancellacomandi(func):
    @wraps(func)
    def wrapped(bot, update):
        if update.message.text is not None:
          if update.message.text.startswith("/"):
            bot.delete_message(update.message.chat_id, update.message.message_id)
        return func(bot, update)
    return wrapped
#OWNERBOT
OWNER_LIST= [44222507, 33003926]

def ownerbot(func):
    @wraps(func)
    def wrapped(bot, update):
        user_id = update.effective_user.id
        if user_id not in OWNER_LIST:
            print("Unauthorized access denied for {}.".format(user_id))
            text_markdown = "`" + 'Utente non riconosciuto' + "`"
            update.message.reply_markdown(text_markdown)
            return
        return func(bot, update)
    return wrapped

#COMANDI PRIVATI
def private(fn):
  def wrapper(*args,**kwargs):
    message = args[1].message
    if message.chat.type == 'private':
      return fn(*args,**kwargs)
    else:
      return False
  return wrapper
#CLASSE MWT PER IL DECORATOR CHE TROVA AUTOMATICAMENTE ADMIN
class MWT(object):
    """Memoize With Timeout"""
    _caches = {}
    _timeouts = {}

    def __init__(self,timeout=2):
        self.timeout = timeout

    def collect(self):
        """Clear cache of results which have timed out"""
        for func in self._caches:
            cache = {}
            for key in self._caches[func]:
                if (time.time() - self._caches[func][key][1]) < self._timeouts[func]:
                    cache[key] = self._caches[func][key]
            self._caches[func] = cache

    def __call__(self, f):
        self.cache = self._caches[f] = {}
        self._timeouts[f] = self.timeout

        def func(*args, **kwargs):
            kw = sorted(kwargs.items())
            key = (args, tuple(kw))
            try:
                v = self.cache[key]
                print("cache")
                if (time.time() - v[1]) > self.timeout:
                    raise KeyError
            except KeyError:
                print("new")
                v = self.cache[key] = f(*args,**kwargs),time.time()
            return v[0]
        func.func_name = f.__name__

        return func
#CONTROLLER ADMIN
@MWT(timeout=10*10)
def get_admin_ids(bot, chat_id):
    """Returns a list of admin IDs for a given chat. Results are cached for 1 hour."""
    return [admin.user.id for admin in bot.get_chat_administrators(chat_id)]
#DECORATOR ADMIN
def admin_id(func):
    @wraps(func)
    def wrapped(bot, update):
      if update.message.from_user.id in get_admin_ids(bot, update.message.chat_id):
        return func(bot, update)
    return wrapped
