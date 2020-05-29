from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
from frontend.setup import frontend


def get_markup():
    markup = InlineKeyboardMarkup(row_width=3)

    activities_near_but = InlineKeyboardButton(
        text="Активности поблизости",
        callback_data="mainmenu_activities_near")

    find_buddies_but = InlineKeyboardButton(
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

    markup.add(activities_near_but, find_buddies_but)
    markup.add(activities_but, buddies_but)
    markup.add(settings_but, stats_but)

    return markup


# Обработчик кнопки Активности поблизости
@frontend.callback_query_handler(
    lambda call: call.data.startswith("mainmenu_activities"))
def activities_near_button_pressed(call):
    frontend.send_message(
        call.message.chat.id,
        "Активности поблизости")


# Обработчик кнопки Поиск приятелей
@frontend.callback_query_handler(
    lambda call: call.data.startswith("mainmenu_find_buddies"))
def find_buddies_button_pressed(call):
    frontend.send_message(
        call.message.chat.id,
        "Поиск приятелей")


# Обработчик кнопки Активности
@frontend.callback_query_handler(
    lambda call: call.data.startswith("mainmenu_activities"))
def activities_button_pressed(call):
    frontend.send_message(
        call.message.chat.id,
        "Активности")


# Обработчик кнопки Мои приятели
@frontend.callback_query_handler(
    lambda call: call.data.startswith("mainmenu_buddies"))
def buddies_button_pressed(call):
    frontend.send_message(
        call.message.chat.id,
        "Мои приятели")


# Обработчик кнопки Настройки аккаунта
@frontend.callback_query_handler(
    lambda call: call.data.startswith("mainmenu_settings"))
def settings_button_pressed(call):
    frontend.send_message(
        call.message.chat.id,
        "Настройки аккаунта")


# Обработчик кнопки Статистика
@frontend.callback_query_handler(
    lambda call: call.data.startswith("mainmenu_stats"))
def stats_button_pressed(call):
    frontend.send_message(
        call.message.chat.id,
        "Статистика")
