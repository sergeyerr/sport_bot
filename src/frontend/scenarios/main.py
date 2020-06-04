from telebot import logger 
from frontend.setup import frontend
from frontend.scenarios import sign_up
from frontend.ui_components import main_menu
from frontend.ui_components import transition_controller
from bot_core import bot

transition_controller.use()


def use():
    """
        Функция нужна, чтобы линтер не возмущался
        по поводу неиспользуемого модуля.
        Да, я гений мысли.
    """
    pass


@frontend.message_handler(commands=['menu', 'start'])
def route(message):
    if not bot.user_exists(message.chat.id):
        logger.info("Launching sign_up scenario from main.py")
        sign_up.launch(message)
    else:
        t, m = main_menu.create_message()
        frontend.send_message(message.chat.id, t, reply_markup=m)
