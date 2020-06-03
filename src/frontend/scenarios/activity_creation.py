import telebot
from telebot import types
#from frontend.setup import frontend
from data.activity import Activity
from bot_core import bot


frontend = telebot.TeleBot('1209584769:AAFqOGx-Vl28QDG_rFHhR2PosOO3DxSHmnk')


new_activity = Activity()


@frontend.message_handler(commands=['start'])
def start_command(message):
    launch_scenario(message)


# Пользователь нажимает кноку - запускается функция
# по созданию мероприятия
def launch_scenario(message):
    markup = types.ReplyKeyboardMarkup(
        resize_keyboard=True,
        one_time_keyboard=True)
    markup.add('Ходьба', 'Бег', 'Велопрогулка', 'Велоспорт')

    frontend.send_message(
        message.chat.id,
        'Выберите тип мероприятия', reply_markup=markup)
    frontend.register_next_step_handler(message, type_step)


# Пользователь выбирает тип мероприятия
def type_step(message):
    type = message.text

    if type in ('Ходьба', 'Бег', 'Велопрогулка', 'Велоспорт'):
        new_activity.type = type
        frontend.send_message(
            message.chat.id,
            'Введите дистанцию',
            reply_markup=types.ReplyKeyboardRemove())
        frontend.register_next_step_handler(message, distance_step)
    else:
        msg = frontend.reply_to(
            message,
            'Кнопка не была нажата. Нажмите кнопку, пожалуйста')
        frontend.register_next_step_handler(msg, type_step)
        return


def distance_step(message):
    pass


frontend.polling()
