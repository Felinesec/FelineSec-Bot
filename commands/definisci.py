import wikipedia as wiki

def definisci_handler(bot, update):
    
    # Recupero della definizione
    arg = update.message.text[12:]
    definizione = wiki.summary(arg)
    
    # Risposta del Bot
    update.message.reply_text(definizione)
    
    # LOG del bot
    user = update.message.from_user
    messagetime = datetime.strftime(datetime.today(), '%H:%M del %d/%m/%Y')
    print('User: {} con ID: {} '.format(user['username'], user['id'])
          + "Ha appena eseguito il seguente comando: /example alle ore " + messagetime)
    
