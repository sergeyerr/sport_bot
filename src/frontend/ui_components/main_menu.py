from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
from frontend.setup import frontend


def create_message():
    markup = InlineKeyboardMarkup(row_width=3)

    activitiesNear_but = InlineKeyboardButton(
        text="Активности поблизости",
        callback_data="mainmenu_activities_nearby")

    findBuddies_but = InlineKeyboardButton(
        text="Найти приятелей",
        callback_data="mainmenu_find_buddies")

    activities_but = InlineKeyboardButton(
        text="Мои активности",
        callback_data="mainmenu_activities")

    buddies_but = InlineKeyboardButton(
        text="Мои приятели",
        callback_data="mainmenu_buddies")

    settings_but = InlineKeyboardButton(
        text="Настройки аккаунта",
        callback_data="mainmenu_settings")

    stats_but = InlineKeyboardButton(
        text="Статистика",
        callback_data="mainmenu_stats")

    markup.add(
        activitiesNear_but, findBuddies_but)

    markup.add(
        activities_but, buddies_but)

    markup.add(
        settings_but, stats_but)

    return "Меню", markup


# Обработчик кнопки Активности поблизости
@frontend.callback_query_handler(
    lambda call: call.data.startswith("mainmenu_activities_nearby"))
def __activities_near_button_pressed(call):
    frontend.send_message(
        call.message.chat.id,
        "Активности поблизости")
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
    frontend.send_message(
        call.message.chat.id,
        "Статистика")
    frontend.answer_callback_query(call.id)
