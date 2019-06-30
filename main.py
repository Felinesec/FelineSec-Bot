#!/usr/bin/env python3
from telegram.ext import Updater, CommandHandler
from time import time
from datetime import timedelta, datetime
from psutil import cpu_percent, virtual_memory, boot_time
import config

    # Comandi del bot
def server_handler(bot, update):
    # if update.message.from_user.id in admin_list:
    text = (
        "Ecco qua le statistiche del server:\n\n"
        "CPU: " + str(cpu_percent())+"%\n"
        "RAM: " + str(virtual_memory().percent)+"%\n"
        "Uptime: " + str( 
            timedelta(
                seconds=(time() - boot_time())
            )
        )+"\n"
        "Boot time: " + str(
            datetime.fromtimestamp(
                boot_time()
            ).strftime("%Y-%m-%d %H:%M:%S")
        )
    )
    update.message.reply_text(text)
    user = update.message.from_user
    messagetime = datetime.strftime(datetime.today(), '%H:%M del %d/%m/%Y')
    print('User: {} con ID: {} '.format(user['username'], user['id'])
          + "Ha appena eseguito il seguente comando: /server alle ore " + messagetime)

def start_handler(bot, update):
    text = (
        "Benvenuto!\nEcco qua una lista dei comandi disponibili:\n"
        "/server\n"
        "Per altre informazioni fai /help"
    )
    update.message.reply_text(text)
    user = update.message.from_user
    messagetime = datetime.strftime(datetime.today(), '%H:%M del %d/%m/%Y')
    print('User: {} con ID: {} '.format(user['username'], user['id'])
          + "Ha appena eseguito il seguente comando: /start alle ore " + messagetime)

def help_handler(bot, update):
    text="/server = Indica le principali statistiche del server (Uptime, utilizzo della cpu e della ram)"
    update.message.reply_text(text)
    user = update.message.from_user
    messagetime = datetime.strftime(datetime.today(), '%H:%M %d/%m/%Y')
    print('User: {} con ID: {} '.format(user['username'], user[
        'id']) + "Ha appena eseguito il seguente comando: /help alle ore " + messagetime)



def main():
    starttime = datetime.strftime(datetime.today(), '%H:%M del %d/%m/%Y')
    print("Bot avviato con successo alle", starttime)
    # Token del bot
    updater = Updater(config.BOT_TOKEN)

    # Updater "trigger"
    updater.dispatcher.add_handler(CommandHandler('server', server_handler))
    updater.dispatcher.add_handler(CommandHandler('start', start_handler))
    updater.dispatcher.add_handler(CommandHandler('help', help_handler))

    # Updater generale
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()