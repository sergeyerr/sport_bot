from telebot import types
from frontend.setup import frontend
from bot_core import bot
from frontend.ui_components import main_menu
from data.user import User


new_users = {
    # user_id: user
}


# Запуск регистрации
def launch(message):
    user_id = message.chat.id

    if message.from_user.last_name is None:
        message.from_user.last_name = ""
    user_name = str(message.chat.first_name)
    if message.chat.last_name is not None:
        user_name += message.chat.last_name

    new_user = User(
        id=user_id,
        name=user_name,
        username=f'@{message.chat.username}'
    )

    new_users[user_id] = new_user

    frontend.send_message(
        message.chat.id,
        'Здравствуйте! Пожалуйста, введите Ваш возраст')
    frontend.register_next_step_handler(message, age_step)


# Обработка указанного возраста
def age_step(message):
    age = message.text

    if not age.isdigit():
        msg = frontend.reply_to(
            message,
            'Возраст должен быть числом. Пожалуйста, повторите попытку')
        frontend.register_next_step_handler(msg, age_step)
        return

    new_users[message.chat.id].age = int(age)

    markup = types.ReplyKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=True)
    markup.add('Мужской', 'Женский')

    frontend.send_message(
        message.chat.id, 'Введите Ваш пол', reply_markup=markup)
    frontend.register_next_step_handler(message, gender_step)


# Обработка указанного пола
def gender_step(message):
    gender = message.text

    if gender in ('Мужской', 'Женский'):
        new_users[message.chat.id].gender = gender
        frontend.send_message(
            message.chat.id,
            'Введите город проживания',
            reply_markup=types.ReplyKeyboardRemove())
        frontend.register_next_step_handler(message, city_step)
    else:
        msg = frontend.reply_to(
            message,
            'Кнопка не была нажата. Нажмите кнопку, пожалуйста')
        frontend.register_next_step_handler(msg, gender_step)
        return


# Обработка указанного города проживания
def city_step(message):
    city = message.text

    new_users[message.chat.id].city = city

    frontend.send_message(
        message.chat.id,
        'Отправьте предпочтительное место для '
        'занятий физической культурой. '
        'Если у Вас не получается это сделать, то зайдите с мобильной версии')
    frontend.register_next_step_handler(message, coord_step)


# Обработка указанной геопозиции
def coord_step(message):
    coord = message.location

    if not (coord is None):
        new_users[message.chat.id].x = message.location.longitude
        new_users[message.chat.id].y = message.location.latitude

        new_user = new_users[message.chat.id]
        bot.create_user(new_user)

        m = frontend.send_message(
            message.from_user.id, f'Отлично, {new_user.name}' +
                                  f'\nВозраст: {str(new_user.age)}' +
                                  f'\nПол: {new_user.gender}' +
                                  f'\nГород: {new_user.city}')
        finalize(m)

    else:
        msg = frontend.reply_to(
            message,
            'Пожалуйста, отправьте геопозицию')
        frontend.register_next_step_handler(msg, coord_step)


def finalize(message):
    t, m, _ = main_menu.create_message()
    frontend.send_message(message.chat.id, t, reply_markup=m)
