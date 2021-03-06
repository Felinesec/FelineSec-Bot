<h1 align="center">
  <a>
    <img alt="felineseclogo" src="https://firebasestorage.googleapis.com/v0/b/project-web-test-server.appspot.com/o/img%2Flogo.svg.png?alt=media&token=8c4c791a-1d8d-40c4-9036-fedd11f7afae" width="250" height="320">
  </a>
  <br><br> FelineSec Bot <br>
</h1>

[![Python3.7+](https://img.shields.io/badge/Python-3.7%2B-green.svg)](https://www.python.org/downloads) ![GitHub release](https://img.shields.io/github/release-pre/Felinesec/FelineSec-Bot.svg?color=blue&style=popout) ![Passing](https://img.shields.io/badge/Build-Passing-brightgreen.svg) [![License: MPL 2.0](https://img.shields.io/badge/License-MPL%202.0-brightgreen.svg)](https://opensource.org/licenses/MPL-2.0) [![Group](https://img.shields.io/badge/Group-%40FelineSec-blue.svg)](https://t.me/FelineSec) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/95904091c7e24a16a0a68c88a344b15e)](https://www.codacy.com/app/Felinesec/FelineSec-Bot?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Felinesec/FelineSec-Bot&amp;utm_campaign=Badge_Grade)



### :thought_balloon: ​Comandi

##### I Comandi già impostati sono:

+ **/start** per l'avvio del bot
+ **/help** per avere una lista dei comandi disponibili
+ **/wiki {arg}** per cercare su wikipedia
+ **/setrules {arg}** per impostare le regole
+ **/rules** per vedere le regole
+ **/server** per avere le statistiche d'uso del server _( CPU, RAM, Uptime, Boot Time)_
+ **/help**: Mostra un riassunto dei comandi
+ **/ping**: effetua un ping su *google.com*


### :memo: Come creare un comando

Per creare un comando serve per prima cosa creare il file del comando _example.py_ sotto la cartella _commands_, poi la struttura del comando dovrà essere:



```python
#!/usr/bin/env python3
#   example.py
#   Python 3.7
#   Version 0.1
#
#   Created by UsernameExample
#   Mozilla Public License
#

#Inserire le librerie da utilizzare


def example_handler(bot, update):
    #TODO: Scrivere il codice del comando
    text = "Example test"
    
    #Risposta del bot in chat
    update.message.reply_text(text)
    
    # LOG del bot
    user = update.message.from_user
    messagetime = datetime.strftime(datetime.today(), '%H:%M del %d/%m/%Y')
    print('User: {} con ID: {} '.format(user['username'], user['id'])
          + "Ha appena eseguito il seguente comando: /example alle ore " + messagetime)
    
 
```

Poi nel file _main.py_ importare il nuovo comando e sotto **#trigger** aggiungere:

```python
from commands import start, server, help, example <----

def main():
    ...
    
    # Trigger
    updh = updater.dispatcher.add_handler
    dp = updater.dispatcher
    updh(CommandHandler('start', start.start_handler))
    updh(CommandHandler('server', server.server_handler))
    updh(CommandHandler('help', help.help_handler))
 -> updh(CommandHandler('example', example.example_handler))  
    dp.add_handler(MessageHandler(None, newuser.newuser_handler))
    dp.add_error_handler(error)
    ...
   
```

Infine nel file *__init__.py* aggiungiamo il nostro comando:

```python
__all__ = ["help", "start", "server", "newuser", "example"] <-

from commands import *
```

### :gear: ​Config

Nel file _example.config.py_ c'è la configurazione di ad esempio **Bot Token** e **Admin List**, l'admin list contiene gli **id** degli utenti amministratori.

### :open_file_folder: ​Project Tree

```markdown

+  bot
|
├── +  commands
|   |    __init__.py
|   |    build_menu.py
|   |    definisci.py
│   |    help.py
|   |    kill.py
│   |    newuser.py
|   |    ping.py
│   |    server.py
|   |    setrules.py
│   |    start.py
|   └───
|
├── +  admins
|   |    __init__.py
|   |    decorator.py
|   └───
| 
|     example.config.py
|     main.py
|     LICENSE.md
|     README.md
|     requirements.txt
|     startup.sh
└───

```

### :heavy_exclamation_mark: Requirements

+ psutil
+ python-telegram-bot
+ datetime
+ wikipedia
+ ping3



