from sys import argv
from pathlib import Path

import telebot

default_token_path = "resources/telegram_bot_token"

token = None
if Path(default_token_path).exists():
    with open(default_token_path) as f:
        token = f.readline()
elif len(argv) == 2:
    token = argv[1]

if token is not None:
    frontend = telebot.TeleBot(token)
else:
    raise ValueError("Could not locate the token to launch the bot")
