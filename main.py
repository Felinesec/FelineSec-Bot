#!/usr/bin/env python3
#   example.config.py
#   Python 3.7
#   Version 0.1
#
#   Created by Francesco Masala & Jack Rendor
#   Mozilla Public License
#
from telegram.ext import Updater, CommandHandler
from time import time
from datetime import timedelta, datetime
from psutil import cpu_percent, virtual_memory, boot_time
import config
import bot_commands



def main():
    starttime = datetime.strftime(datetime.today(), '%H:%M del %d/%m/%Y')
    print("Bot avviato con successo alle", starttime)
    # Token del bot
    updater = Updater(config.BOT_TOKEN)

    # Updater "trigger"
    updater.dispatcher.add_handler(CommandHandler('server', bot_commands.server_handler))
    updater.dispatcher.add_handler(CommandHandler('start', bot_commands.start_handler))
    updater.dispatcher.add_handler(CommandHandler('help', bot_commands.help_handler))

    # Updater generale
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()