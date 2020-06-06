from sys import argv
from pathlib import Path

import telebot
import os


default_token_path = "resources/telegram_bot_token"

token = None
if Path(default_token_path).exists():
    with open(default_token_path) as f:
        token = f.readline()
elif len(argv) == 2:
    token = argv[1]
# Используется для настройки Heroku
elif os.environ.get('TG_TOKEN'):
    token = os.environ.get('TG_TOKEN')

if token is not None:
    if os.environ.get('TOR'):
        telebot.apihelper.proxy = {'https': '//127.0.0.1:9080'}
    frontend = telebot.TeleBot(token)
else:
    raise ValueError("Could not locate the token to launch the bot")
