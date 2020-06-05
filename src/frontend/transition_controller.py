"""
    В данном файле в неявном виде
    описаны все возможные переходы
    между компонентами в функционирующем меню.
"""

from telebot import logger

from frontend.setup import frontend
from frontend.ui_components import stats_display
from frontend.ui_components import main_menu
from frontend.ui_components import activity_viewer
from bot_core import bot

def use():
    """
        Функция нужна, чтобы линтер не возмущался
        по поводу неиспользуемого модуля.
        Да, я гений мысли.
    """
    pass


# Обработчики клавиш главного меню

# Обработчик кнопки Активности поблизости
@frontend.callback_query_handler(
    lambda call: call.data.startswith("mainmenu_activities_nearby"))
def __activities_near_button_pressed(call):
    _, m, loc = activity_viewer.create_message()
    frontend.send_location(
        call.message.chat.id,
        loc[0], loc[1],
        reply_markup=m)
    frontend.answer_callback_query(call.id)


# Обработчик кнопки Поиск приятелей
@frontend.callback_query_handler(
    lambda call: call.data.startswith("mainmenu_find_buddies"))
def __find_buddies_button_pressed(call):

    frontend.send_message(
        call.message.chat.id,
        "Поиск приятелей")
    frontend.answer_callback_query(call.id)


# Обработчик кнопки Активности
@frontend.callback_query_handler(
    lambda call: call.data.startswith("mainmenu_activities"))
def __find_button_pressed(call):
    frontend.send_message(
        call.message.chat.id,
        "Активности")
    frontend.answer_callback_query(call.id)


# Обработчик кнопки Мои приятели
@frontend.callback_query_handler(
    lambda call: call.data.startswith("mainmenu_buddies"))
def __buddies_button_pressed(call):
    frontend.send_message(
        call.message.chat.id,
        "Мои приятели")
    frontend.answer_callback_query(call.id)


# Обработчик кнопки Настройки аккаунта
@frontend.callback_query_handler(
    lambda call: call.data.startswith("mainmenu_settings"))
def __settings_button_pressed(call):
    frontend.send_message(
        call.message.chat.id,
        "Настройки аккаунта")
    frontend.answer_callback_query(call.id)


# Обработчик кнопки Статистика
@frontend.callback_query_handler(
    lambda call: call.data.startswith("mainmenu_stats"))
def __stats_button_pressed(call):
    u = bot.get_user_by_id(call.message.chat.id)
    t, m, p = stats_display.create_message(u)
    frontend.send_photo(
        call.message.chat.id, p, t, reply_markup=m)
    frontend.answer_callback_query(call.id)


# Обработчики просмотрщика статистики

@frontend.callback_query_handler(
    lambda call: call.data.startswith("stats_display_back"))
def __user_viewer_back_button_pressed(call):
    frontend.delete_message(call.message.chat.id, call.message.message_id)
    logger.info("Deleting stats_display message")
    frontend.answer_callback_query(call.id)


# Обработчики просмотрщика активностей

@frontend.callback_query_handler(
    func=lambda call: call.data.startswith("activity_viewer_back"))
def __go_back_button_pressed(call):
    frontend.delete_message(call.message.chat.id, call.message.message_id)
    frontend.answer_callback_query(call.id)


@frontend.callback_query_handler(
    func=lambda call: call.data.startswith("activity_viewer_participants"))
def __participants_button_pressed(call):
    # ВЫВЕСТИ СПИСОК УЧАСТНИКОВ СОБЫТИЯ (ПО ТАБЛИЦЕ ACTIVITIES)
    frontend.answer_callback_query(call.id)
