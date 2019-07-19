import wikipedia as wiki
from datetime import datetime


def definisci_handler(bot, update):
    
    # Recupero della definizione
    arg = update.message.text[5:]
    wiki.set_lang('it')
    definizione = wiki.summary(arg)
    p = wiki.page(arg)

    text = "**{}**\n{}".format(p.title, definizione}

    # Risposta del Bot
    update.message.reply_text(text)
    
    # LOG del bot
    user = update.message.from_user
    messagetime = datetime.strftime(datetime.today(), '%H:%M del %d/%m/%Y')
    print('User: {} con ID: {} '.format(user['username'], user['id'])
          + "Ha appena eseguito il seguente comando: /wiki alle ore " + messagetime)
    

