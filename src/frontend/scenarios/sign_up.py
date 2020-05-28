from telebot import types
from frontend.setup import frontend
from bot_core import bot

from frontend.ui_components.main_menu import main_menu
from data.user import User


new_user = User()


@frontend.message_handler(commands=['start'])
def start_command(message):
    if not bot.user_exists(message.chat.id):
        launch_scenario(message)
    else:
        finalize(message)


def launch_scenario(message):
    user_id = message.chat.id

    if message.from_user.last_name is None:
        message.from_user.last_name = ""
    user_name = message.from_user.first_name + \
                ' ' + message.from_user.last_name

    new_user.id = user_id
    new_user.name = user_name
    new_user.username = f'@{message.chat.username}'

    frontend.send_message(
        message.chat.id,
        'Здравствуйте! Пожалуйста, введите Ваш возраст')
    frontend.register_next_step_handler(message, age_step)


def age_step(message):
    age = message.text

    if not age.isdigit():
        msg = frontend.reply_to(
            message,
            'Возраст должен быть числом. Пожалуйста, повторите попытку')
        frontend.register_next_step_handler(msg, age_step)
        return

    new_user.age = int(age)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add('Мужской', 'Женский')

    frontend.send_message(
        message.chat.id, 'Введите Ваш пол', reply_markup=markup)
    frontend.register_next_step_handler(message, gender_step)


def gender_step(message):
    gender = message.text

    if gender in ('Мужской', 'Женский'):
        new_user.gender = gender
        frontend.send_message(
            message.chat.id,
            'Введите город проживания', reply_markup=types.ReplyKeyboardRemove())
        frontend.register_next_step_handler(message, city_step)
    else:
        msg = frontend.reply_to(
            message,
            'Кнопка не была нажата. Нажмите кнопку, пожалуйста')
        frontend.register_next_step_handler(msg, gender_step)
        return


def city_step(message):
    city = message.text

    new_user.city = city

    frontend.send_message(
        message.chat.id,
        'Отправьте предпочтительное место для '
        'занятий физической культурой')
    frontend.register_next_step_handler(message, coord_step)


def coord_step(message):
    coord = message.location

    if not (coord is None):
        new_user.x = message.location.longitude
        new_user.y = message.location.latitude
        bot.save_user(new_user)
        finalize(message)

        frontend.send_message(
            message.from_user.id, f'Отлично, {new_user.name}' +
                                  f'\nВозраст: {str(new_user.age)}' +
                                  f'\nПол: {new_user.gender}' +
                                  f'\nГород: {new_user.city}')
    else:
        msg = frontend.reply_to(
            message,
            'Пожалуйста, отправьте геопозицию')
        frontend.register_next_step_handler(msg, coord_step)
        return


def finalize(message):
    """ Высылает пользователю главное меню """
    frontend.send_message(message.chat.id, "Меню", reply_markup=main_menu())
    pass
