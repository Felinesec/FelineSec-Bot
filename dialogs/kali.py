#   kali.py
#   Python 3.7
#   Version 0.1
#
#   Created by Francesco Masala and Hersel Giannella
#   Mozilla Public License
#
def init(update, context):
    bot = context.bot
    bot.send_message(update.message.chat_id,
                     text="Complimenti {user} ora sei autistico!"
                     .format(user=update.message.from_user.first_name),
                     parse_mode='HTML')
