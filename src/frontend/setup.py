import logging

import telebot

logger = telebot.logger
telebot.logger.setLevel(logging.INFO)

token_path = "resources/telegram_bot_token"

frontend = telebot.TeleBot("")

if __name__ == "__main__":
    try:
        with open(token_path) as f:
            t = f.readline()
        frontend = telebot.TeleBot(t)
    except Exception as e:
        logger.exception(e)
