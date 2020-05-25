from telebot import types
from frontend.setup import frontend
from bot_core import bot

# Этот файл из прототипа рабочий,
# но имеет некоторые проблемы.
# 1. Здесь производятся обращение напрямую
#    моделям ORM. Это противоречит идее
#    архитектора (который только и может, что писать длинные комментарии, которые никто не читает).
#    Требуется убрать все обращения напрямую к моделям ORM из этого
#    файла и создать для них функции в файле bot_core/bot.py
# 2. Требуется переписать этот код, чтобы он использовал
#    InlineKeyboardMarkup из telebot.types.
# 3. И кто такой этот new_users?? Если не нужен, удали.


new_users = {}


@frontend.message_handler(commands=['start'])
def __start_command(message):
    if not bot.user_exists(message.chat.id):
        launch_scenario(message)
    else:
        __finalize()


def launch_scenario(message):
    user_id = message.chat.id
    print(message)
    if message.from_user.last_name is None:
        message.from_user.last_name = ""
    user_name = message.from_user.first_name + \
        ' ' + \
        message.from_user.last_name
    chat_link = f'@{message.chat.username}'
    new_users[user_id] = User(id=user_id, name=user_name, link=chat_link)
    frontend.send_message(
        message.chat.id,
        'Здравствуйте! Пожалуйста, введите Ваш возраст.')
    frontend.register_next_step_handler(message, __age_step)


def __age_step(message):
    user_id = message.chat.id
    age = message.text
    if not age.isdigit():
        msg = frontend.reply_to(
            message,
            'Возраст должен быть числом. Пожалуйста, повторите попытку')
        frontend.register_next_step_handler(msg, __age_step)
        return
    user = new_users[user_id]
    user.age = age
    new_users[user_id] = user
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add('Мужской', 'Женский')
    frontend.send_message(
        message.chat.id, 'Введите Ваш пол', reply_markup=markup)
    frontend.register_next_step_handler(message, __gender_step)


def __gender_step(message):
    user_id = message.from_user.id
    gender = message.text
    user = new_users[user_id]
    if gender in ('Мужской', 'Женский'):
        user.gender = gender
        user.save(force_insert=True)
        __finalize()
        frontend.send_message(
            user_id, f'Отлично, {user.name},' +
            '\nВозраст: {str(user.age)}' +
            '\nПол: {user.gender}')
    else:
        msg = frontend.reply_to(
            message,
            'Кнопка не была нажата. Нажмите кнопку, пожалуйста.')
        frontend.register_next_step_handler(msg, __gender_step)
        return


def __finalize():
    """ Высылает пользователю главное меню """

    pass
