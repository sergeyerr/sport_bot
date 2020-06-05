from telebot import types
from frontend.setup import frontend
from data.activity import Activity
from bot_core import bot
from datetime import datetime
from frontend.ui_components import main_menu


new_activities = {
    # chat_id: new_activity
}


# Пользователь нажимает кноку - запускается функция
# по созданию мероприятия
def launch(user_id):
    markup = types.ReplyKeyboardMarkup(
        resize_keyboard=True,
        one_time_keyboard=True)
    markup.add('Ходьба', 'Бег', 'Велопрогулка', 'Велоспорт')

    new_activities[user_id] = Activity()

    message = frontend.send_message(
        user_id,
        'Выберите тип мероприятия', reply_markup=markup)
    frontend.register_next_step_handler(message, type_step)


# Обработка указанного типа мероприятия
def type_step(message):
    type = message.text

    if type in ('Ходьба', 'Бег', 'Велопрогулка', 'Велоспорт'):
        new_activities[message.chat.id].type = type

        # !!!
        new_activities[message.chat.id].estimated_time = 0

        frontend.send_message(
            message.chat.id,
            'Введите дистанцию в КМ',
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
        new_activities[message.chat.id].distance = float(distance)

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
        new_activities[message.chat.id].x = message.location.longitude
        new_activities[message.chat.id].y = message.location.latitude

        frontend.send_message(
            message.chat.id,
            'Введите дату и время в формате ДД/ММ/ГГГГ ЧЧ:ММ')
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
        datetime.strptime(date, '%d/%m/%Y %H:%M')
        return True
    except Exception:
        return False


# Обработка указанной даты и времени
def time_step(message):
    date = message.text

    if is_date_time(date):
        new_activities[message.chat.id].date = datetime.strptime(date, '%d/%m/%Y %H:%M')

        msg = frontend.send_message(
            message.chat.id,
            "Придумайте название для мероприятия!")
        frontend.register_next_step_handler(msg, name_step)
    else:
        msg = frontend.reply_to(
            message,
            'Пожалуйста, введите дату и время '
            'в формате ДД/ММ/ГГГГ ЧЧ:ММ')
        frontend.register_next_step_handler(msg, time_step)
        return


def name_step(message):
    name = message.text

    new_activities[message.chat.id].name = name
    bot.create_activity(new_activities[message.chat.id])

    finalize(message)


# Если все ок, высылает уведомление
def finalize(message):
    markup = types.InlineKeyboardMarkup()
    item = types.InlineKeyboardButton(
        "В меню", callback_data='activity_creation_back')
    markup.add(item)

    frontend.send_message(
        message.chat.id,
        text='Мероприятие успешно добавлено!',
        reply_markup=markup)
