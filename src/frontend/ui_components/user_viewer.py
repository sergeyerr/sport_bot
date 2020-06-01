import math

from telebot import types
from frontend.frontend import frontend

users = list(map(lambda x: {
    "id": x,
    "name": f"name{x}",
    "age": 20,
    "link": "what?",
    "distance": 0,
    "activity": [f"Activity{x}"]
}, range(10)))


USERS_PER_CARD = 3


def create_message(users):
    pointer = 0
    return (__recreate_markup(users, pointer), __message_text(users, pointer))


def __parse_switch_call_data(users, call):
    parts = call.data.split("_", 4)
    if len(parts) == 3:
        try:
            p = int(parts[2])
            total_pages = math.ceil(len(users) // USERS_PER_CARD)
            if p < 0 or p > total_pages:
                return None
            else:
                return p
        except Exception:
            return 0


def __update_markup(users, call):
    message = call.message
    p = __parse_switch_call_data(users, call)
    if p is not None:
        frontend.edit_message_text(
            chat_id=message.chat.id,
            message_id=message.message_id,
            text=__message_text(users, p),
            reply_markup=__recreate_markup(users, p))


def __message_text(users, pointer):
    page_number = pointer + 1
    total_pages = math.ceil(len(users) // USERS_PER_CARD)
    return f'Страница {page_number}/{int(total_pages)}'


def __recreate_markup(users, pointer):
    markup = types.InlineKeyboardMarkup()

    offset = pointer * USERS_PER_CARD
    index = pointer
    for user in users[offset:USERS_PER_CARD+offset]:
        uinfo = f"{user['name']}, {user['link']}, {str(user['age'])}"
        udist = str(int(user['distance'])) + 'км'
        activities = ' '.join(user['activity'])
        text = f"{uinfo}, {udist}, {activities}"
        markup.add(types.InlineKeyboardButton(
            text=text,
            callback_data=f'userviewer_select_{offset + index}'))
        index += 1

    return __append_nav_buttons(markup, pointer)


def __append_nav_buttons(markup, pointer):
    buttons = []
    buttons.append(
        types.InlineKeyboardButton(
            text='Предыдущий',
            callback_data=f'userviewer_prev_{pointer-1}'))
    buttons.append(
        types.InlineKeyboardButton(
            text='Следующий',
            callback_data=f'userviewer_next_{pointer+1}'))
    markup.add(*buttons)

    return markup


@frontend.callback_query_handler(
    func=lambda call: call.data.startswith("userviewer_next"))
def __next_button_pressed(call):
    __update_markup(users, call)
    frontend.answer_callback_query(call.id)


@frontend.callback_query_handler(
    func=lambda call: call.data.startswith("userviewer_prev"))
def __prev_button_pressed(call):
    __update_markup(users, call)
    frontend.answer_callback_query(call.id)


@frontend.callback_query_handler(
    func=lambda call: call.data == "userviewer_cancel")
def __cancel_button_pressed(call):
    pass
