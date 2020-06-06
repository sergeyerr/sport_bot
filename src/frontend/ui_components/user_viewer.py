import math

from telebot import types
from frontend.setup import frontend
from bot_core import bot

instances = {
    # message_id: user_list
}


USERS_PER_CARD = 3


def create_component(message_id, user_a, users):
    instances[message_id] = users
    return (
        __message_text(users, 0),
        __recreate_markup(user_a, users, 0), None)


def drop_component(message_id):
    if message_id in instances:
        del instances[message_id]


def __parse_switch_call_data(users, call):
    parts = call.data.split("_", 4)
    if len(parts) == 3:
        try:
            p = int(parts[2])
            total_pages = math.ceil(len(users) / USERS_PER_CARD)
            if p < 0 or p >= total_pages:
                return None
            else:
                return p
        except Exception:
            return 0


def __update_markup(user_a, users, call):
    message = call.message
    p = __parse_switch_call_data(users, call)
    if p is not None:
        frontend.edit_message_text(
            chat_id=message.chat.id,
            message_id=message.message_id,
            text=__message_text(users, p),
            reply_markup=__recreate_markup(user_a, users, p))


def __message_text(users, pointer):
    page_number = pointer + 1
    total_pages = math.ceil(len(users) / USERS_PER_CARD)
    return f'Страница {page_number}/{int(total_pages)}'


def __recreate_markup(user_a, users, pointer):
    markup = types.InlineKeyboardMarkup(row_width=5)

    offset = pointer * USERS_PER_CARD
    index = 0
    for user in users[offset:USERS_PER_CARD+offset]:
        uinfo = f"{user.username}, {str(user.age)}"
        udist = str(round(bot.user_distance(user_a, user))) + ' км'
        text = f"{uinfo}, {udist}"
        markup.add(types.InlineKeyboardButton(
            text=text,
            callback_data=f'userviewer_select_{users[offset + index].id}'))
        index += 1

    markup = __append_nav_buttons(markup, pointer)

    markup.add(types.InlineKeyboardButton(
        text="Назад",
        callback_data="userviewer_back"
    ))

    return markup


def __append_nav_buttons(markup, pointer):
    buttons = []
    buttons.append(
        types.InlineKeyboardButton(
            text='<<',
            callback_data=f'userviewer_prev_{pointer-1}'))
    buttons.append(
        types.InlineKeyboardButton(
            text='>>',
            callback_data=f'userviewer_next_{pointer+1}'))
    markup.add(*buttons)

    return markup


@frontend.callback_query_handler(
    func=lambda call: call.data.startswith("userviewer_next"))
def __next_button_pressed(call):
    users = instances.get(call.message.message_id)
    user_a = bot.get_user_by_id(call.message.chat.id)
    if users is not None:
        __update_markup(user_a, users, call)
    frontend.answer_callback_query(call.id)


@frontend.callback_query_handler(
    func=lambda call: call.data.startswith("userviewer_prev"))
def __prev_button_pressed(call):
    users = instances.get(call.message.message_id)
    user_a = bot.get_user_by_id(call.message.chat.id)
    if users is not None:
        __update_markup(user_a, users, call)
    frontend.answer_callback_query(call.id)
