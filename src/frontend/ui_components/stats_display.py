from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

# Пример словаря
# _user = {
#     'name': 'Алексей',
#     'age': '21',
#     'city':'Perm',
#     'activitiesFinished':'5',
#     'favouriteSport':'Пиво',
#     'cityRating': '2'
# }


def create_message(user_dict):
    markup = InlineKeyboardMarkup()

    # Тащим кнопку и ее колбэк
    markup.add(InlineKeyboardButton(
        "Назад", callback_data="stats_display_back"))

    # Сама текстовая часть сообщения, если чего-то не будет -
    # будет выдавать None (должно)
    message_text =\
        f"{user_dict.get('name')}, {user_dict.get('age')} лет,\n" +\
        f"{user_dict.get('city')},\n" +\
        f"Законченных активностей: {user_dict.get('activitiesFinished')},\n" +\
        f"Любимый вид спорта: {user_dict.get('favouriteSport')},\n" +\
        f"Место в городе: {user_dict.get('cityRating')}"

    # Кортеж из всех данных для сообщения
    return (message_text, markup)

# Пример вызова всего кортежа в одном сообщении:
# frontend.send_photo(
#   message.chat.id,
#   workingtuple[2],
#   caption=workingtuple[1],
#   reply_markup=workingtuple[0])
# При желании можно попытаться прикрутить маркдаун,
# но он че то не пашет (parse_mode="Markdown")
# СЛЕДИТЬ ЗА ТЕМ, ЧТОБЫ СТРОКИ НЕ БЫЛИ ДЛИННЕЕ 79 СИМВОЛОВ!
