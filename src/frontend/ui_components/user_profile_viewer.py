"""
    Компонент, который показывает пользователю
    информацию о другом пользователе и предоставляет
    возможность добавить или удалить пользователя
    из списка товарищей.
"""

from telebot import logger
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

from frontend import util
from frontend.setup import frontend
from data.user import User
from bot_core import bot


# Обязательная функция.
def create_component(user_a: User, user_b: User) -> tuple:
    """
        Возвращает разметку компонента и
        текст сообщения, в котором разметка будет расположена.

        Аргументы
        ----------
        user: dict
            Словарь с данными пользователя.

        Возвращаемые значения
        ---------------------
        тройка: (message_text, message_markup, file_id)
    """

    markup = None
    if not bot.one_way_buddies(user_a, user_b):
        markup = create_markup_add(user_a.id, user_b.id)
    else:
        markup = create_markup_delete(user_a.id, user_b.id)

    # Создание сообщения (для вывода данных пользователя)
    message = "Пользователь\n"
    message += user_b.username + "\n"
    message += str(user_b.age) + "\n"
    message += user_b.gender + "\n"
    message += user_b.city

    file_id = util.user_picture(user_b.id)

    return (message, markup, file_id)


# Функция для создания markup c кнопкой добавить в приятели
def create_markup_add(user_a_id, user_b_id):
    markup = InlineKeyboardMarkup(row_width=3)

    add_buddy_but = InlineKeyboardButton(
        text="Добавить в приятели",
        callback_data=f"user_profile_viewer_add_buddy_{user_a_id}_{user_b_id}")

    cancel_but = InlineKeyboardButton(
        text="Назад",
        callback_data="user_profile_viewer_cancel")

    markup.add(add_buddy_but)
    markup.add(cancel_but)
    return markup


# Функция для создания markup c кнопкой удалить из приятелей
def create_markup_delete(user_a_id, user_b_id):
    markup = InlineKeyboardMarkup(row_width=3)

    delete_buddy_but = InlineKeyboardButton(
        text="Удалить из приятелей",
        callback_data=f"user_profile_viewer_delete_buddy_{user_a_id}"
        f"_{user_b_id}")

    cancel_but = InlineKeyboardButton(
        text="Назад",
        callback_data="user_profile_viewer_cancel")

    markup.add(delete_buddy_but)
    markup.add(cancel_but)

    return markup


# Обработчик кнопки "Добавить в приятели"
@frontend.callback_query_handler(
    lambda call: call.data.startswith("user_profile_viewer_delete_buddy"))
def delete_buddy_button_pressed(call):
    ba, bb = __parse_change_buddy_status_data(call.data)
    logger.info(f"Unbudding {bb} from {ba}")
    bot.unbud(ba, bb)

    # Создание нового markup для обновления старого
    markup = create_markup_add(ba, bb)

    # Обновление старого markup
    frontend.edit_message_reply_markup(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        reply_markup=markup)

    frontend.answer_callback_query(call.id)


# Обработчик кнопки "Удалить из приятелей"
@frontend.callback_query_handler(
    lambda call: call.data.startswith("user_profile_viewer_add_buddy"))
def add_buddy_button_pressed(call):
    ba, bb = __parse_change_buddy_status_data(call.data)
    logger.info(f"Budding {bb} to {ba}")
    bot.bud(ba, bb)

    # Создание нового markup для обновления старого
    markup = create_markup_delete(ba, bb)

    # Обновление старого markup
    frontend.edit_message_reply_markup(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        reply_markup=markup)

    frontend.answer_callback_query(call.id)


def __parse_change_buddy_status_data(data):
    vs = data.split('_')
    return vs[5], vs[6]
