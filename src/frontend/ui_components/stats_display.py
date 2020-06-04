from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
from frontend import util


def create_message(user):
    # markup = InlineKeyboardMarkup()

    # Тащим кнопку и ее колбэк
    # markup.add(InlineKeyboardButton(
    #     "Назад", callback_data="stats_display_back"))

    # Сама текстовая часть сообщения, если чего-то не будет -
    # будет выдавать None (должно)
    message_text =\
        f"{user.name}, {user.age} лет,\n" +\
        f"{user.city},\n" +\
        f"Законченных активностей: {'Unknown'},\n" +\
        f"Любимый вид спорта: {'Unknown'},\n" +\
        f"Место в городе: {'Unknown'}"

    picture = util.user_picture(user.id)

    # Кортеж из всех данных для сообщения
    return (message_text, None, picture)
