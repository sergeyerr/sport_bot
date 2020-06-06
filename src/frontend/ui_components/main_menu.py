from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup


def create_message():
    markup = InlineKeyboardMarkup(row_width=3)

    activities_near_but = InlineKeyboardButton(
        text="Активности рядом",
        callback_data="mainmenu_activities_nearby")

    findBuddies_but = InlineKeyboardButton(
        text="Найти приятелей",
        callback_data="mainmenu_find_buddies")

    activities_but = InlineKeyboardButton(
        text="Мои активности",
        callback_data="mainmenu_activities")

    buddies_but = InlineKeyboardButton(
        text="Мои приятели",
        callback_data="mainmenu_buddies")

    new_activity_but = InlineKeyboardButton(
        text="Создать актив!",
        callback_data="mainmenu_new_activity")

    stats_but = InlineKeyboardButton(
        text="Статистика",
        callback_data="mainmenu_stats")

    update_profile_but = InlineKeyboardButton(
        text="Обновить профиль",
        callback_data="mainmenu_update_profile"
    )

    markup.add(
        activities_near_but, findBuddies_but)

    markup.add(
        activities_but, buddies_but)

    markup.add(
        new_activity_but, stats_but)

    markup.add(update_profile_but)

    return "Меню", markup, None
