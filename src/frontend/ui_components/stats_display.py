from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
from data.user import User
from frontend.ui_components.util import get_user_picture

# Функция должна возвращать строку, в которой
# описана статистика пользователя.
# Нужно использовать информацию в таблице User.
# Если в таблице нет того, что есть в макете интерфейса,
# то пишем, как в макете.

def get_message_text(userDict, frontend, message):
	#пример словаря: userDict = {'name': 'Алексей', 'age': '21', 'city':'Perm', 'activitiesFinished':'5', 'favouriteSport':'Пиво', 'cityRating': '2'}

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Назад", callback_data="stats_display_back")) #тащим кнопку и ее колбэк
    
    message_text = '%s, %s лет, %s\nЗаконченных активностей: %s\nЛюбимый вид спорта: %s\nМесто в городе: %s' % (userDict.get('name'), userDict.get('age'), userDict.get('city'), userDict.get('activitiesFinished'), userDict.get('favouriteSport'), userDict.get('cityRating'))
    #сама текстовая часть сообщения, если чего-то не будет - будет выдавать None (должно)
    
    file_id = get_user_picture(frontend, message) #достаем айди аватарки
        
    return (markup, message_text, file_id) #кортеж из всех данных для сообщения

#Пример вызова всего кортежа в одном сообщении:
#frontend.send_photo(message.chat.id, workingtuple[2], caption=workingtuple[1], reply_markup=workingtuple[0])
#При желании можно попытаться прикрутить маркдаун, но он че то не пашет (parse_mode="Markdown")
# СЛЕДИТЬ ЗА ТЕМ, ЧТОБЫ СТРОКИ НЕ БЫЛИ ДЛИННЕЕ 79 СИМВОЛОВ!
