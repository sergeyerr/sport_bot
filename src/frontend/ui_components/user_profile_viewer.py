"""
    Компонент, который показывает пользователю
    информацию о другом пользователе и предоставляет
    возможность добавить или удалить пользователя
    из списка товарищей.
"""

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

from frontend.setup import frontend

# Этот компонент показывается пользователю после того,
# как пользователь выберет кого-нибудь в компоненте
# user_viewer. В данном файле нужно реализовать разметку
# компонента минимум с кнопкми "bud" и "cancel".
# Кнопка "bud" становится "unbud" после добавления
# человека в товарищи, поэтому нужно реализовать обновление
# разметки в обработчиках.


# Предполагаем, что в словаре user
# будут все данные, которые показаны
# на макете. Ключи для словаря называем исходя
# из названий в макете.
# Обязательная функция.
def create_message(user: User):
    """
        Возвращает разметку компонента и
        текст сообщения, в котором разметка будет расположена.

        Аргументы
        ----------
        user: dict
            Словарь с данными пользователя.

        Возвращаемые значения
        ---------------------
        пара: (message_text, message_markup)
    """

    # Ваш код
    markup = InlineKeyboardMarkup(row_width=3)

    addBuddy_but = InlineKeyboardButton(
        text="Добавить в приятели",
        callback_data="user_profile_viewer_addBuddy")

    cancel_but = InlineKeyboardButton(
        text="Назад",
        callback_data="user_profile_viewer_cancel")

    markup.add(addBuddy_but)
    markup.add(cancel_but)

    return ("Пользователь", markup)
    pass


# Обратите внимание на формат call.data
@frontend.callback_query_handler(
    lambda call: call.data.startswith("user_profile_viewer_cancel"))
def activities_near_button_pressed(call):
    # Этот обработчик реализовывать не нужно
    # Вызов answer_callback_query должен быть в конце каждого обработчика.
    frontend.answer_callback_query(call.id)
