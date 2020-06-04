import telebot
import os


frontend = None


def create_frontend(token):
    global frontend
    if os.environ.get('TOR'):
        from telebot import apihelper
        apihelper.proxy = {'https': '//127.0.0.1:9080'}
    frontend = telebot.TeleBot(token)


def start_frontend():
    frontend.polling()
