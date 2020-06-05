"""
    Компонент, который показывает пользователю
    информацию о другом пользователе и предоставляет
    возможность добавить или удалить пользователя
    из списка товарищей.
"""

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

from frontend.setup import frontend

from data.user import User

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

#Функция для создания markup c кнопкой добавить в приятели
def create_markup_add():
    markup = InlineKeyboardMarkup(row_width=3)

    addBuddy_but = InlineKeyboardButton(
        text="Добавить в приятели",
        callback_data="user_profile_viewer_addBuddy")

    cancel_but = InlineKeyboardButton(
        text="Назад",
        callback_data="user_profile_viewer_cancel")

    markup.add(addBuddy_but)
    markup.add(cancel_but)
    return markup

#Функция для создания markup c кнопкой удалить из приятелей
def create_markup_delete():
    
    markup = InlineKeyboardMarkup(row_width=3)

    deleteBuddy_but = InlineKeyboardButton(
        text="Удалить из приятелей",
        callback_data="user_profile_viewer_deleteBuddy")

    cancel_but = InlineKeyboardButton(
        text="Назад",
        callback_data="user_profile_viewer_cancel")

    markup.add(deleteBuddy_but)
    markup.add(cancel_but)
    return markup



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
    markup = create_markup_add()

    #Создание сообщения (для вывода данных пользователя)
    message = "Пользователь\n"
    message += user.username + "\n"
    message += str(user.age) + "\n"
    message += user.gender+ "\n"
    message += user.city

    return (message, markup)
    pass

     
#Тестовый обработчик сообщений
#@frontend.message_handler(func = lambda message: True)
#def test(message):
#    testuser = User()
#    testuser.username ="Vlad"
#    testuser.age = 19
#    testuser.gender ="Male"
#    testuser.city ="Perm"
#    x = create_message(testuser)
#    frontend.send_message(
#    message.chat.id,x[0], reply_markup=x[1])


#Обработчик кнопки "Добавить в приятели"
@frontend.callback_query_handler(
    lambda call: call.data.startswith("user_profile_viewer_addBuddy"))
def addBuddy_button_pressed(call):

    #Создание нового markup для обновления старого
    markup = create_markup_delete()

    #Обновление старого markup
    frontend.edit_message_reply_markup(chat_id=call.message.chat.id,
    message_id=call.message.message_id, reply_markup= markup)

    frontend.answer_callback_query(call.id)


#Обработчик кнопки "Удалить из приятелей"
@frontend.callback_query_handler(
    lambda call: call.data.startswith("user_profile_viewer_deleteBuddy"))
def addBuddy_button_pressed(call):

    #Создание нового markup для обновления старого
    markup = create_markup_add()

    #Обновление старого markup
    frontend.edit_message_reply_markup(chat_id=call.message.chat.id,
    message_id=call.message.message_id, reply_markup= markup)

    frontend.answer_callback_query(call.id)


#Обработчик кнопки "Назад"
# Обратите внимание на формат call.data
@frontend.callback_query_handler(
    lambda call: call.data.startswith("user_profile_viewer_cancel"))
def activities_near_button_pressed(call):
    # Этот обработчик реализовывать не нужно
    # Вызов answer_callback_query должен быть в конце каждого обработчика.
    frontend.answer_callback_query(call.id)
