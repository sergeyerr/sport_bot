from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
from data.user import User

markup = InlineKeyboardMarkup()
markup.add(InlineKeyboardButton("Назад", callback_data="stats_display_back"))


# Функция должна возвращать строку, в которой
# описана статистика пользователя.
# Нужно использовать информацию в таблице User.
# Если в таблице нет того, что есть в макете
# интерфейса, то пишем, как в макете.
def get_message_text():
    pass


# СЛЕДИТЬ ЗА ТЕМ, ЧТОБЫ СТРОКИ НЕ БЫЛИ ДЛИННЕЕ 79 СИМВОЛОВ!
