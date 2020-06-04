import telebot

frontend = None


def create_frontend(token):
    global frontend
    frontend = telebot.TeleBot(token)


def start_frontend():
    frontend.polling()
