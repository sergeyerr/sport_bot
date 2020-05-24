from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
from frontend.setup import frontend

# Нужно записать сюда все кнопки главного меню
# С указанием callback_data, как в примере.
markup = InlineKeyboardMarkup()
markup.add([
    [InlineKeyboardButton(
        "Активности поблизости",
        callback_data="main_menu_activities"), ...],
    [], ...
])


# Для каждой кнопки подготовить заготовку обработчика.
@frontend.callback_query_handler(
    lambda call: call.data.startswith("main_menu_activities"))
def __activities_button_pressed(call):
    pass

# СЛЕДИТЬ ЗА ТЕМ, ЧТОБЫ СТРОКИ НЕ БЫЛИ ДЛИННЕЕ 79 СИМВОЛОВ!
