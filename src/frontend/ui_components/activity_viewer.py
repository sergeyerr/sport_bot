"""
    Графический компонент, который представляет пользователю
    мероприятия с возможностью записаться на них.
"""

from frontend.setup import frontend
from bot_core.bot import get_all_activities
from bot_core.bot import participate_in_activity, quit_activity, is_participating
from telebot import types
# Запись на мероприятие должна добавлять соответствующую запись
# в таблицу activities.

all_activities = get_all_activities()
pointer = 0


def __update_markup(call):
    message = call.message
    activity_id = int(call.data.split('_')[3])

    global pointer
    if activity_id < 0:
        activity_id = 0
    elif activity_id >= len(all_activities):
        activity_id = len(all_activities)-1

    if pointer != activity_id:
        pointer = activity_id
        frontend.edit_message_live_location(latitude=all_activities[pointer].x,
                                            longitude=all_activities[pointer].y,
                                            chat_id=message.chat.id,
                                            message_id=message.message_id,
                                            reply_markup=get_activities_markup())


def get_activities_markup():
    markup = types.InlineKeyboardMarkup()
    text = f"{all_activities[pointer].type}, {all_activities[pointer].distance}km, {all_activities[pointer].date}"
    markup.add(types.InlineKeyboardButton(text=text, callback_data='smth'))



    buttons = []
    buttons.append(
        types.InlineKeyboardButton(
            text='Предыдущий',
            callback_data=f'activity_viewer_prev_{pointer - 1}'))

    join_button_text = 'Присоединиться'
    if is_participating(1, pointer):
        join_button_text = 'Покинуть'

    buttons.append(
        types.InlineKeyboardButton(
            text=join_button_text,
            callback_data=f'join_activity_{pointer}'))
    buttons.append(
        types.InlineKeyboardButton(
            text='Следующий',
            callback_data=f'activity_viewer_next_{pointer + 1}'))
    buttons.append(
        types.InlineKeyboardButton(
            text='Назад',
            callback_data=f'go_back'))
    buttons.append(
        types.InlineKeyboardButton(
            text='Участники',
            callback_data=f'participants_{pointer}'))
    markup.add(*buttons)
    return markup


def create_message(message):
    """
        Возвращает разметку компонента и
        текст сообщения, в котором разметка будет расположена.

        Возвращаемые значения
        ---------------------
        пара: (message_text, message_markup)
    """
    #  А ВОТ И НЕ ВОЗВРАЩАЕТ РАЗМЕТКУ, МЕТОД ОТПРАВЛЯЕТ LOCATION И РАЗМЕТКУ, А ПОТОМ LOCATION МЕНЯЕТСЯ, ДАЛЬШЕ ДУМАЙ САМ КАК ДЕЛАТЬ

    cur_msg = frontend.send_location(message.chat.id, all_activities[0].x, all_activities[0].y, live_period=86400,
                                     reply_markup=get_activities_markup())


@frontend.callback_query_handler(
    func=lambda call: call.data.startswith("activity_viewer_prev"))
def __prev_button_pressed(call):
    __update_markup(call)
    frontend.answer_callback_query(call.id)


@frontend.callback_query_handler(
    func=lambda call: call.data.startswith("activity_viewer_next"))
def __next_button_pressed(call):
    __update_markup(call)
    frontend.answer_callback_query(call.id)


@frontend.callback_query_handler(
    func=lambda call: call.data.startswith("join_activity"))
def __join_button_pressed(call):
    if is_participating(1, int(call.data.split('_')[2])):
        quit_activity(1, int(call.data.split('_')[2]))
    else:
        participate_in_activity(1, int(call.data.split('_')[2]))

    frontend.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                       reply_markup=get_activities_markup())
    frontend.answer_callback_query(call.id)


@frontend.callback_query_handler(
    func=lambda call: call.data.startswith("go_back"))
def __go_back_button_pressed(call):
    # ЗАГРУЗИТЬ МЕНЮ
    frontend.answer_callback_query(call.id)


@frontend.callback_query_handler(
    func=lambda call: call.data.startswith("participants"))
def __participants_button_pressed(call):
    #ВЫВЕСТИ СПИСОК УЧАСТНИКОВ СОБЫТИЯ (ПО ТАБЛИЦЕ ACTIVITIES)
    frontend.answer_callback_query(call.id)


@frontend.callback_query_handler(
    lambda call: call.data.startswith("activity_viewer_viewer_cancel"))
def activities_near_button_pressed(call):
    # Этот обработчик реализовывать не нужно
    # Данный вызов должен быть в конце каждого обработчика.
    frontend.answer_callback_query(call.id)
