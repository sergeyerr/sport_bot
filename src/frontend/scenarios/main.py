from telebot import logger
from frontend.setup import frontend
from frontend.scenarios import sign_up
from frontend.scenarios import activity_creation
from frontend.ui_components import main_menu
from frontend.ui_components import user_profile_viewer
from frontend import transition_controller
from bot_core import bot

transition_controller.use()


def use():
    """
        Функция нужна, чтобы линтер не возмущался
        по поводу неиспользуемого модуля.
        Да, я гений мысли.
    """
    pass


def handle_new_user(message):
    if not bot.user_exists(message.chat.id):
        logger.info("Launching sign_up scenario from main.py")
        sign_up.launch(message)
        return True
    else:
        return False


@frontend.message_handler(commands=['menu', 'start'])
def route_start(message):
    if not handle_new_user(message):
        logger.info("Sending main_menu to the user from main.py")
        t, m, _ = main_menu.create_message()
        frontend.send_message(message.chat.id, t, reply_markup=m)


@frontend.message_handler(commands=['new_activity'])
def route_create_activity(message):
    if not handle_new_user(message):
        activity_creation.launch(message)


@frontend.message_handler(commands=['activities'])
def route_list_activities(message):
    if not handle_new_user(message):
        logger.info("Listing the user's activities")
        pass


@frontend.callback_query_handler(lambda call: call.data == 'none')
def handle_no_call_data(call):
    frontend.answer_callback_query(
        call.id, "Спасибо, что выбрали наш продукт!")
