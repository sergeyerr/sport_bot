from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
from frontend import util
from bot_core.bot import get_top_user_activity, get_finished_user_activities, get_top_by_activity

def create_message(user):
    markup = InlineKeyboardMarkup()

    # Тащим кнопку и ее колбэк
    markup.add(InlineKeyboardButton(
        "Назад", callback_data="stats_display_back"))

    # Сама текстовая часть сообщения, если чего-то не будет -
    # будет выдавать None (должно)
    top_activity = get_top_user_activity(user.id)
    total_activities = get_finished_user_activities(user.id)
    top_list = get_top_by_activity(top_activity)
    if len(top_activity) == 0:
        top_activity = 'Ещё не участвовали в спортивных активностях'
    else:
        top_activity = top_activity[0].type

    if len(total_activities) == 0:
        total_activities = 0
    else:
        total_activities = total_activities[0].totalcount

    if len(top_list) == 0:
        top_list = 'Вы непревзойдённы в прокрастинации'
    else:
        flag = True
        for i in range(len(top_list)):
            if top_list[i].username == user.username:
                top_list = i + 1
                flag = False
                break
        if flag:
            top_list = 'Вы непревзойдённы в прокрастинации'


    message_text = \
        f"{user.name}, {user.age} лет,\n" + \
        f"{user.city},\n" + \
        f"Законченных активностей: {total_activities},\n" + \
        f"Любимый вид спорта: {top_activity},\n" + \
        f"Место в городе: {top_list}"

    picture = util.user_picture(user.id)

    # Кортеж из всех данных для сообщения
    return (message_text, markup, picture)
