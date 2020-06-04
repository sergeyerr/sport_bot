import logging
import telebot
import os

from src.frontend import setup

logger = telebot.logger
telebot.logger.setLevel(logging.INFO)

# Используется для настройки heroku
if os.environ.get('TG_TOKEN'):
    token = os.environ.get('TG_TOKEN')
else:
    with open("resources/telegram_bot_token") as f:
        token = f.readline()

try:
    setup.create_frontend(token)
    setup.start_frontend()
except Exception as e:
    logger.exception(e)
