import logging

from telebot import logger

from frontend.setup import frontend
from frontend.scenarios import main

main.use()

logger.setLevel(logging.INFO)

try:
    frontend.polling()
except Exception as e:
    logger.exception(e)
