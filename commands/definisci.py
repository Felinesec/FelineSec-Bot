import wikipedia as wiki
from datetime import datetime
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def build_menu(buttons,
               n_cols,
               header_buttons=None,
               footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, [header_buttons])
    if footer_buttons:
        menu.append([footer_buttons])
    return menu

def definisci_handler(bot, update):
    
    # Recupero della definizione
    arg = update.message.text[5:]
    wiki.set_lang('it')
    pg = wiki.page(wiki.search(arg)[0])
    title = pg.title
    pg_url = pg.url
    definizione = pg.summary

    link_btn = InlineKeyboardButton("View on Wikipedia", url=pg_url)
    
    reply_markup = InlineKeyboardMarkup(build_menu(link_btn, n_cols=1))

    text = "*{}:*\n\n{}".format(title, definizione)

    # Risposta del Bot
    update.message.reply_markdown(text, reply_markup=reply_markup)
    
    # LOG del bot
    user = update.message.from_user
    messagetime = datetime.strftime(datetime.today(), '%H:%M del %d/%m/%Y')
    print('User: {} con ID: {} '.format(user['username'], user['id'])
          + "Ha appena eseguito il seguente comando: /wiki alle ore " + messagetime)
    

