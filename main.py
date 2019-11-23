#   main.py
#   Python 3.7
#   Version 0.3 "Acrux"
#
#   Created by Francesco Masala, Jack Rendor and Hersel Giannella
#   Mozilla Public License
#
import config
import json
import logging
import dialogs, utils
from commands import start, server, help, definisci, rules, setrules, kill, ping, ban, ip
from datetime import datetime
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackQueryHandler
import telegram


def rules_button(update, context):
    bot = context.bot
    with open('commands/felinesec.rules.json') as f:
        data = json.load(f)

    query = update.callback_query
    rules = data['rules']
    if query.data == "rules":
        bot.send_message(query.message.chat_id,"*Regole:*\n\n{rules_txt}".format(rules_txt=rules), parse_mode=telegram.ParseMode.MARKDOWN)

def main():


    # Messaggio di avvio
    starttime = datetime.strftime(datetime.today(), '%H:%M del %d/%m/%Y')
    print("Il bot e' stato avviato con successo alle :", starttime)

    # Token del Bot
    updater = Updater(config.bot_token, use_context=True)

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
    updh(CommandHandler('kill', kill.kill_handler))
    updh(CommandHandler('ping', ping.ping_handler))
    updh(CommandHandler('ban', ban.ban_handler))
    updh(CommandHandler('ip', ip.ipshodan_handler))


    dp.add_handler(CallbackQueryHandler(rules_button))
    dp.add_handler(MessageHandler(None, dialogs.handler.init))

    # Updater
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()




if __name__ == "__main__":
    main()
