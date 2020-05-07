#   private_command.py
#   Python 3.7
#   Version 0.3 "Acrux"
#
#   Created by Francesco Masala and Hersel Giannella
#   Mozilla Public License
#
from functools import wraps
#PRIVATE COMMAND
def init(fn):
  def wrapper(*args,**kwargs):

    message = args[0].message
    if message.chat.type == 'private':
      return fn(*args,**kwargs)
    else:
      return False
  return wrapper
