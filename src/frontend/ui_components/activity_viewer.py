"""
    Графический компонент, который представляет пользователю
    мероприятия с возможностью записаться на них.
"""

from telebot import logger
from frontend.setup import frontend
from bot_core.bot import get_all_activities
from bot_core.bot import (
    participate_in_activity,
    quit_activity,
    is_participating
)
from telebot import types, apihelper


instances = {
    # message_id: activity_list
}


def create_component(message_id, user_id, activities):
    """
        Возвращает разметку компонента и
        текст сообщения, в котором разметка будет расположена.

        Возвращаемые значения
        ---------------------
        кортеж: (message_text, message_markup, (x, y))
    """

    instances[message_id] = (user_id, activities)
    x = activities[0].x
    y = activities[0].y

    p = False
    if is_participating(user_id, activities[0].id):
        p = True

    return ("Локация", __activity_markup(activities, 0, p), (x, y))


def drop_component(message_id):
    if message_id in instances:
        del instances[message_id]


def __activity_markup(activities, pointer, is_participating):
    markup = types.InlineKeyboardMarkup()
    d = activities[pointer].date
    text = \
        f"{activities[pointer].type}, " \
        f"{activities[pointer].distance}km, " \
        f"{d.date().day}.{d.date().month}.{d.date().year} {d.time()}"
    markup.add(types.InlineKeyboardButton(text=text, callback_data="none"))

    join_button_text = 'Добавиться'
    if is_participating:
        join_button_text = 'Покинуть'

    buttons = [
        types.InlineKeyboardButton(
            text='←',
            callback_data=f'activity_viewer_prev_{pointer}_{pointer - 1}'),
        types.InlineKeyboardButton(
            text=join_button_text,
            callback_data=f'activity_viewer_join_activity_{pointer}'),
        types.InlineKeyboardButton(
            text='→',
            callback_data=f'activity_viewer_next_{pointer}_{pointer + 1}'),
        types.InlineKeyboardButton(
            text='Назад',
            callback_data=f'activity_viewer_back'),
        types.InlineKeyboardButton(
            text='Участники',
            callback_data=f'activity_viewer_participants'
            f'_{activities[pointer].id}')
    ]

    markup.add(*buttons)

    return markup


def __update_markup(message, old_pointer, new_pointer):
    user_id, activities = instances[message.message_id]
    p = False
    if is_participating(user_id, activities[new_pointer].id):
        p = True

    frontend.edit_message_live_location(
        latitude=activities[new_pointer].x,
        longitude=activities[new_pointer].y,
        chat_id=message.chat.id,
        message_id=message.message_id,
        reply_markup=__activity_markup(activities, new_pointer, p))


def __try_switch(call):
    _, activities = instances[call.message.message_id]

    op, np = __parse_next_prev_data(call.data)
    if np < 0 or np >= len(activities) or np == op:
        return False

    op, p = __parse_next_prev_data(call.data)
    __update_markup(call.message, op, p)

    return True


@frontend.callback_query_handler(
    func=lambda call: call.data.startswith("activity_viewer_prev"))
def __prev_button_pressed(call):
    alert_text = None
    if not __try_switch(call):
        alert_text = "Показано самое первое мероприятие"
    frontend.answer_callback_query(call.id, alert_text)


@frontend.callback_query_handler(
    func=lambda call: call.data.startswith("activity_viewer_next"))
def __next_button_pressed(call):
    alert_text = None
    if not __try_switch(call):
        alert_text = "Показано последнее мероприятие"
    frontend.answer_callback_query(call.id, alert_text)


@frontend.callback_query_handler(
    func=lambda call: call.data.startswith("activity_viewer_join_activity"))
def __join_button_pressed(call):
    if call.message.message_id in instances:
        user_id, activities = instances[call.message.message_id]
        pointer = __parse_join_activity_data(call.data)
        activity_id = activities[pointer].id

        p = False
        if is_participating(user_id, activity_id):
            logger.info(f"Unlisting user from activity #{activity_id}")
            quit_activity(user_id, activity_id)
            p = False
        else:
            logger.info(f"Enlisting user in activity #{activity_id}")
            participate_in_activity(user_id, activity_id)
            p = True

        try:
            frontend.edit_message_reply_markup(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                reply_markup=__activity_markup(activities, pointer, p))
        except apihelper.ApiException as e:
            print(e)

    frontend.answer_callback_query(call.id)


def __parse_join_activity_data(data):
    vs = data.split('_')
    return int(vs[4])


def __parse_next_prev_data(data):
    vs = data.split('_')
    return int(vs[3]), int(vs[4])
