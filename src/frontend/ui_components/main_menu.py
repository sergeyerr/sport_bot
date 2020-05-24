from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
from frontend.setup import frontend

# Нужно записать сюда все кнопки главного меню
markup = InlineKeyboardMarkup(row_width=3)

@frontend.message_handler(func = lambda message: True)
def mainMenu(message):
    
    activitiesNear_but = InlineKeyboardButton(
    text ="Активности поблизости",
    callback_data ="activitiesNear")

    findBuddies_but = InlineKeyboardButton(
    text ="Найти приятелей",
    callback_data ="findBuddies")

    activities_but = InlineKeyboardButton(
    text ="Мои активности",
    callback_data ="activities")

    buddies_but = InlineKeyboardButton(
    text ="Мои приятели",
    callback_data ="buddies")

    settings_but = InlineKeyboardButton(
    text ="Настройки аккаунта",
    callback_data ="settings")

    stats_but = InlineKeyboardButton(
    text ="Статистика", 
    callback_data ="stats")

    markup.add(
    activitiesNear_but,findBuddies_but)

    markup.add(
    activities_but,buddies_but)

    markup.add(
    settings_but, stats_but)

    frontend.send_message(
    message.chat.id,"Меню", reply_markup=markup)


# Для каждой кнопки подготовить заготовку обработчика.

# Обработчик кнопки Активности поблизости
@frontend.callback_query_handler(
    lambda call: call.data.startswith("activitiesNear"))
def activitiesNear_but_pressed(call): 
    
    frontend.send_message(
    call.message.chat.id,
    "Активности поблизости")

# Обработчик кнопки Поиск приятелей
@frontend.callback_query_handler(
    lambda call: call.data.startswith("findBuddies"))
def activitiesNear_but_pressed(call): 
    
    frontend.send_message(
    call.message.chat.id,
    "Поиск приятелей")

# Обработчик кнопки Активности
@frontend.callback_query_handler(
    lambda call: call.data.startswith("activities"))
def activitiesNear_but_pressed(call): 
    
    frontend.send_message(
    call.message.chat.id,
    "Активности")

# Обработчик кнопки Мои приятели
@frontend.callback_query_handler(
    lambda call: call.data.startswith("buddies"))
def activitiesNear_but_pressed(call): 
    
    frontend.send_message(
    call.message.chat.id,
    "Мои приятели")

# Обработчик кнопки Настройки аккаунта
@frontend.callback_query_handler(
    lambda call: call.data.startswith("settings"))
def activitiesNear_but_pressed(call): 
    
    frontend.send_message(
    call.message.chat.id,
    "Настройки аккаунта")

# Обработчик кнопки Статистика
@frontend.callback_query_handler(
    lambda call: call.data.startswith("stats"))
def activitiesNear_but_pressed(call): 
    
    frontend.send_message(
    call.message.chat.id,
    "Статистика")

# СЛЕДИТЬ ЗА ТЕМ, ЧТОБЫ СТРОКИ НЕ БЫЛИ ДЛИННЕЕ 79 СИМВОЛОВ!
