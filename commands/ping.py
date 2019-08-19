from ping3 import ping, verbose_ping
from admins import decorator
from datetime import datetime


@decorator.restricted
def ping_handler(bot, update):
    ms = ping('google.com', unit='ms')
    messagetime = datetime.strftime(datetime.today(), '%H:%M del %d/%m/%Y')
    user = update.message.from_user
    text_markdown0 = "`" + 'Pong!' + "`"
    update.message.reply_markdown(text_markdown0)
    text_markdown1 = "`" + str(ms) + ' ms' + "`"
    update.message.reply_markdown(text_markdown1)
    print('User: {} con ID: {} '.format(user['username'], user['id'])
          + "Ha appena eseguito il seguente comando: /ping alle ore " + messagetime)
