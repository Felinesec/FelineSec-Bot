#!/usr/bin/env python3
#   rules.py
#   Python 3.7
#   Version 0.3 "Acrux"
#
#   Created by Francesco Masala
#   Mozilla Public License
#

import json
import config
from datetime import datetime
from shodan import Shodan


def ipshodan_handler(update, context):
    api = config.Shodan
    ip = update.message.text[12:]
    ipinfo = api.host(ip)
    update.message.reply(ipinfo)
