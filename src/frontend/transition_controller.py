"""
    В данном файле в неявном виде
    описаны все возможные переходы
    между компонентами в функционирующем меню.
"""

from telebot import logger

from frontend.setup import frontend
from frontend.scenarios import activity_creation, sign_up

from frontend.ui_components import (
    stats_display,
    user_viewer,
    activity_viewer,
    main_menu,
    user_profile_viewer
)

from bot_core import bot


def use():
    """
        Функция нужна, чтобы линтер не возмущался
        по поводу неиспользуемого модуля.
        Да, я гений мысли.
    """
    pass


# Обработчики клавиш главного меню

def send_activities(
    message,
    activities,
    if_none_message="Мероприятия не найдены"
):
    user_id = message.chat.id

    if len(activities) == 0:
        return False
    else:
        msg = frontend.send_location(message.chat.id, 0, 0, 86400)
        _, m, loc = activity_viewer.create_component(
            msg.message_id, user_id, activities)
        frontend.edit_message_live_location(
            loc[0], loc[1],
            user_id,
            msg.message_id,
            reply_markup=m)

    return True


def send_buddies(
    message,
    buddies,
):
    user_id = message.chat.id
    user = bot.get_user_by_id(user_id)

    if len(buddies) == 0:
        return False
    else:
        msg = frontend.send_message(
            user_id, "Загрузка...")
        t, m, _ = user_viewer.create_component(msg.message_id, user, buddies)
        frontend.edit_message_text(
            t, msg.chat.id, msg.message_id, reply_markup=m)

    return True


# Обработчик кнопки Активности поблизости
@frontend.callback_query_handler(
    lambda call: call.data.startswith("mainmenu_activities_nearby"))
def __activities_near_button_pressed(call):
    alert_text = None
    activities = bot.suggest_activities(call.message.chat.id)

    logger.info("Serving activity_viewer with activities nearby")
    if not send_activities(call.message, activities, alert_text):
        alert_text = "Не найдено ни одно достаточно близкое к Вам мероприятие"

    frontend.answer_callback_query(call.id, alert_text)


# Обработчик кнопки Активности
@frontend.callback_query_handler(
    lambda call: call.data.startswith("mainmenu_activities"))
def __find_button_pressed(call):
    alert_text = None
    activities = bot.activities_by_user(call.message.chat.id)

    logger.info("Serving activity_viewer with user's activities")
    if not send_activities(call.message, activities, alert_text):
        alert_text = "Вы не подписаны ни на одно мероприятие"

    frontend.answer_callback_query(call.id, alert_text)


# Обработчик кнопки Поиск приятелей
@frontend.callback_query_handler(
    lambda call: call.data.startswith("mainmenu_find_buddies"))
def __find_buddies_button_pressed(call):
    alert_text = None
    buddies = bot.suggest_buddies(call.message.chat.id)
    if not send_buddies(call.message, buddies):
        alert_text = 'Не найдено'

    frontend.answer_callback_query(call.id, alert_text)


# Обработчик кнопки Мои приятели
@frontend.callback_query_handler(
    lambda call: call.data.startswith("mainmenu_buddies"))
def __buddies_button_pressed(call):
    alert_text = None
    buddies = bot.buddies_by_user_id(call.message.chat.id)
    if not send_buddies(call.message, buddies):
        alert_text = 'Список Ваших товарищей пуст'
    frontend.answer_callback_query(call.id, alert_text)


# Обработчик кнопки Новая активность аккаунта
@frontend.callback_query_handler(
    lambda call: call.data.startswith("mainmenu_new_activity"))
def __settings_button_pressed(call):
    activity_creation.launch(call.message.chat.id)
    frontend.answer_callback_query(call.id)


# Обработчик кнопки Статистика
@frontend.callback_query_handler(
    lambda call: call.data.startswith("mainmenu_stats"))
def __stats_button_pressed(call):
    u = bot.get_user_by_id(call.message.chat.id)
    t, m, p = stats_display.create_message(u)
    frontend.send_photo(
        call.message.chat.id, p, t, reply_markup=m)
    frontend.answer_callback_query(call.id)


@frontend.callback_query_handler(
    lambda call: call.data.startswith("mainmenu_update_profile")
)
def __update_profile_button_pressed(call):
    sign_up.launch(call.message)


# Обработчики просмотрщика статистики

@frontend.callback_query_handler(
    lambda call: call.data.startswith("stats_display_back"))
def __user_viewer_back_button_pressed(call):
    logger.debug("Deleting stats_display")
    frontend.delete_message(call.message.chat.id, call.message.message_id)
    frontend.answer_callback_query(call.id)


# Обработчики просмотрщика активностей

@frontend.callback_query_handler(
    func=lambda call: call.data.startswith("activity_viewer_back"))
def __go_back_button_pressed(call):
    logger.debug("Deleting activity_viewer")
    frontend.delete_message(call.message.chat.id, call.message.message_id)
    frontend.answer_callback_query(call.id)


@frontend.callback_query_handler(
    func=lambda call: call.data.startswith("activity_viewer_participants"))
def __participants_button_pressed(call):
    alert_text = None
    activity_id = call.data.split('_')[3]
    participants = bot.users_by_activity(activity_id)
    if not send_buddies(call.message, participants):
        alert_text = \
            "В мероприятии никто не участвует. Вы можете стать первым!"

    frontend.answer_callback_query(call.id, alert_text)


# Обработчики просмотрщика пользователей

@frontend.callback_query_handler(
    func=lambda call: call.data == "userviewer_back")
def __cancel_button_pressed(call):
    logger.debug("Deleting user_viewer")
    user_viewer.drop_component(call.message.message_id)
    frontend.delete_message(call.message.chat.id, call.message.message_id)


@frontend.callback_query_handler(
    func=lambda call: call.data.startswith("userviewer_select"))
def __select_button_pressed(call):
    user_id = call.data.split('_')[2]
    logger.debug(
        f"User profile with id {user_id} selected "
        ", serving user_profile_viewer")
    user_a = bot.get_user_by_id(call.message.chat.id)
    user_b = bot.get_user_by_id(user_id)
    t, m, f = user_profile_viewer.create_component(user_a, user_b)
    frontend.send_photo(call.message.chat.id, f, t, reply_markup=m)

    frontend.answer_callback_query(call.id)


# Обработчики создания активностей

# Callback на нажатие кнопки
@frontend.callback_query_handler(
    lambda call: call.data.startswith("activity_creation_back"))
def __activity_creation_back_button_pressed(call):
    t, m, _ = main_menu.create_message()
    frontend.edit_message_text(
        t,
        call.message.chat.id,
        call.message.message_id,
        reply_markup=m)

    # frontend.answer_callback_query(call)


# Обработчики просмотрщика профиля пользователя

@frontend.callback_query_handler(
    lambda call: call.data.startswith("user_profile_viewer_cancel"))
def user_profile_viewer_cancel(call):
    try:
        frontend.delete_message(call.message.chat.id, call.message.message_id)
    except Exception:
        pass

    frontend.answer_callback_query(call.id)
