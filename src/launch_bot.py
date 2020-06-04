import logging

import telebot

from frontend import setup

logger = telebot.logger
telebot.logger.setLevel(logging.INFO)

with open("resources/telegram_bot_token") as f:
    token = f.readline()

try:
    setup.create_frontend(token)
    setup.start_frontend()
except Exception as e:
    logger.exception(e)
