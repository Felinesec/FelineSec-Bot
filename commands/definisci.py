import wikipedia as wiki
from datetime import datetime


def definisci_handler(bot, update):
    
    # Recupero della definizione
    arg = update.message.text[5:]
    wiki.set_lang('it')
    pg = wiki.page(wiki.search(arg)[0])
    title = pg.title
    definizione = pg.summary

    text = "*{}*\n{}".format(title, definizione)

    # Risposta del Bot
    update.message.reply_markdown(text)
    
    # LOG del bot
    user = update.message.from_user
    messagetime = datetime.strftime(datetime.today(), '%H:%M del %d/%m/%Y')
    print('User: {} con ID: {} '.format(user['username'], user['id'])
          + "Ha appena eseguito il seguente comando: /wiki alle ore " + messagetime)
    

