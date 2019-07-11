#!/usr/bin/env python3
#   main.py
#   Python 3.7
#   Version 0.1
#
#   Created by Francesco Masala & Jack Rendor
#   Mozilla Public License
#
import config
import logging
from commands import start, server, help, newuser
from datetime import datetime
from telegram.ext import Updater, CommandHandler, MessageHandler


def main():
    starttime = datetime.strftime(datetime.today(), '%H:%M del %d/%m/%Y')
    print("Il bot e' stato avviato con successo alle :", starttime)

    # Token del Bot
    updater = Updater(config.bot_token)

    # Logging
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    logger = logging.getLogger(__name__)

    def error(update, context):
        logger.warning('Update "%s" generate error: "%s"', update, context.error)

    # Trigger
    updh = updater.dispatcher.add_handler
    dp = updater.dispatcher
    updh(CommandHandler('start', start.start_handler))
    updh(CommandHandler('server', server.server_handler))
    updh(CommandHandler('help', help.help_handler))
    dp.add_handler(MessageHandler(None, newuser.init))
    dp.add_error_handler(error)

    # Updater
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
