from frontend.setup import frontend

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


@frontend.callback_query_handler(
    lambda call: call.data.startswith("stats_display_back"))
def __user_viewer_back_button_pressed(call):
    frontend.send_message(
        call.message.chat.id,
        "Выйти из просмотрщика статистики")
    frontend.answer_callback_query(call.id)
