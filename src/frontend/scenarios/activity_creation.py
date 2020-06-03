import telebot
from telebot import types
# from frontend.setup import frontend
from data.activity import Activity
from bot_core import bot
from datetime import datetime
from frontend.ui_components import main_menu

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


# Обработка указанного типа мероприятия
def type_step(message):
    type = message.text

    if type in ('Ходьба', 'Бег', 'Велопрогулка', 'Велоспорт'):
        new_activity.type = type

        frontend.send_message(
            message.chat.id,
            'Введите дистанцию в км',
            reply_markup=types.ReplyKeyboardRemove())
        frontend.register_next_step_handler(message, distance_step)
    else:
        msg = frontend.reply_to(
            message,
            'Кнопка не была нажата. Нажмите кнопку, пожалуйста')
        frontend.register_next_step_handler(msg, type_step)
        return


# Проверка на число
def is_digit(string):
    if string.isdigit():
        return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False


# Обработка указанной дистанции
def distance_step(message):
    distance = message.text

    if is_digit(distance):
        new_activity.distance = float(distance)

        frontend.send_message(
            message.chat.id,
            'Отправьте место проведения мероприятия')
        frontend.register_next_step_handler(message, coord_step)
    else:
        msg = frontend.reply_to(
            message,
            'Дистанция должна быть числом. Пожалуйста, повторите попытку')
        frontend.register_next_step_handler(msg, distance_step)
        return


# Обработка указанной геопозиции
def coord_step(message):
    coord = message.location

    if not (coord is None):
        new_activity.x = message.location.longitude
        new_activity.y = message.location.latitude

        frontend.send_message(
            message.chat.id,
            'Введите дату и время в формате ДД/ММ/ГГ ЧЧ:ММ')
        frontend.register_next_step_handler(message, time_step)
    else:
        msg = frontend.reply_to(
            message,
            'Пожалуйста, отправьте геопозицию')
        frontend.register_next_step_handler(msg, coord_step)
        return


# Проверка на дату и время
def is_date_time(date):
    try:
        datetime.strptime(date, '%d/%m/%Y %I:%M')
        return True
    except:
        return False


# Обработка указанной даты и времени
def time_step(message):
    date = message.text

    if is_date_time(date):
        new_activity.date = datetime.strptime(date, '%d/%m/%Y %I:%M')

        bot.save_activity(new_activity)
        finalize(message)
    else:
        msg = frontend.reply_to(
            message,
            'Пожалуйста, введите дату и время '
            'в формате ДД/ММ/ГГГГ ЧЧ:ММ')
        frontend.register_next_step_handler(msg, time_step)
        return


# Callback на нажатие кнопки
@frontend.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == 'back':
            frontend.send_message(
                call.message.chat.id, "Меню",
                reply_markup=main_menu.create_message())


# Если все ок, высылает уведомление
def finalize(message):
    markup = types.InlineKeyboardMarkup()
    item = types.InlineKeyboardButton("Назад", callback_data='back')
    markup.add(item)

    frontend.send_message(
        message.chat.id,
        text='Мероприятие успешно добавлено!',
        reply_markup=markup)


frontend.polling()
