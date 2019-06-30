from telegram.ext import Updater, CommandHandler
import psutil, time, datetime
starttime = datetime.datetime.strftime(datetime.datetime.today(), '%H:%M del %d/%m/%Y')
print ("Bot avviato con successo alle " + starttime)

    # Token del bot
updater = Updater('INSERT_TOKEN_HERE')

    # Comandi del bot
def server(bot, update):
    # if update.message.from_user.id in admin_list:
    text="Ecco qua le statistiche del server:\n\n"
    text=text+"CPU: "+str(psutil.cpu_percent())+"%\n"
    text=text+"RAM: "+str(psutil.virtual_memory().percent)+"%\n"
    text=text+"Uptime: "+str(datetime.timedelta(seconds=(time.time() - psutil.boot_time())))+"\n"
    text=text+"Boot time: "+str(datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S"))
    update.message.reply_text(text)
    user = update.message.from_user
    messagetime = datetime.datetime.strftime(datetime.datetime.today(), '%H:%M del %d/%m/%Y')
    print('User: {} con ID: {} '.format(user['username'], user['id'])
          + "Ha appena eseguito il seguente comando: /server alle ore " + messagetime)
def start(bot, update):
    text="Benvenuto!\nEcco qua una lista dei comandi disponibili:\n"
    text=text+"/server\n"
    text=text+"Per altre informazioni fai /help"
    update.message.reply_text(text)
    user = update.message.from_user
    messagetime = datetime.datetime.strftime(datetime.datetime.today(), '%H:%M del %d/%m/%Y')
    print('User: {} con ID: {} '.format(user['username'], user['id'])
          + "Ha appena eseguito il seguente comando: /start alle ore " + messagetime)
def help(bot, update):
    text="/server = Indica le principali statistiche del server (Uptime, utilizzo della cpu e della ram)"
    update.message.reply_text(text)
    user = update.message.from_user
    messagetime = datetime.datetime.strftime(datetime.datetime.today(), '%H:%M %d/%m/%Y')
    print('User: {} con ID: {} '.format(user['username'], user[
        'id']) + "Ha appena eseguito il seguente comando: /help alle ore " + messagetime)

    # Updater "trigger"
updater.dispatcher.add_handler(CommandHandler('server', server))
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))

    # Updater generale
updater.start_polling()
updater.idle()
