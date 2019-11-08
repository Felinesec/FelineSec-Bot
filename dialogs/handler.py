#   handler.py
#   Python 3.7
#   Version 0.3 "Acrux"
#
#   Created by Francesco Masala and Hersel Giannella
#   Mozilla Public License
#
from utils import util
from . import welcome, kali, arch

msg = ""

def trigger(match):
	return msg.lower().startswith(match.lower())

#FUNCTION DECLARATION
def init(update, context):
	global msg

	util.debug(update)
	welcome.init(update, context)

	if update.message is None or update.message.text is None:
		return

	msg = update.message.text

	if trigger("kali linux"):
		kali.init(update, context)
	elif trigger("arch linux"):
		arch.init(update, context)
