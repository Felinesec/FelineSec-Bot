#   main.py
#   Python 3.7
#   Version 0.1
#
#   Created by Francesco Masala & Jack Rendor
#   Mozilla Public License
#
import config
import json
import logging
from commands import start, server, help, newuser, definisci, rules, setrules
from datetime import datetime
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackQueryHandler


def rules_button(bot, update):
    with open('commands/felinesec.rules.json') as f:
        rules = json.load(f)['rules']

    query = update.callback_query
    if query.data == "rules":
        update.message.reply_text(query.message.chat_id, rules)

def main():



    # Messaggio di avvio
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
    updh(CommandHandler('rules', rules.rules_handler))
    updh(CommandHandler('wiki', definisci.definisci_handler))
    updh(CommandHandler('setrules', setrules.setrules_handler))
    dp.add_handler(CallbackQueryHandler(rules_button))
    dp.add_handler(MessageHandler(None, newuser.newuser_handler))
    dp.add_error_handler(error)

    # Updater
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
