#!/usr/bin/env python3
#   build_menu.py
#   Python 3.7
#   Version 0.1
#
#   Created by Talebian & Hersel Giannella
#   Mozilla Public License
#
from . import strings

def debug(update):
  if update.message is not None and update.message.text is not None:
    chat_name=str(update.message.chat.title) 
    chat_id=str(update.message.chat_id) 
    chat_user=str(update.message.chat.username) 
    author_id=str(update.message.from_user.id) 
    author_user=str(update.message.from_user.name) 
    author_name=str(update.message.from_user.first_name)+" "+str(update.message.from_user.last_name) 
    post_text=str(update.message.text)
    print(strings.DEBUG_UPDATE % (chat_name, chat_id, chat_user, author_id, author_user, author_name, post_text))

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