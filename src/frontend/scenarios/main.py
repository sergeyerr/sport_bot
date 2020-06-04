from frontend.setup import frontend
from frontend.scenarios import sign_up
from frontend.ui_components import main_menu
from frontend.ui_components import stats_display
from frontend.ui_components import user_viewer
from frontend.ui_components import transition_controller
from frontend import util
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
def route_menu(message):
    if not bot.user_exists(message.chat.id):
        sign_up.launch(message)
    else:
        t, m = main_menu.create_message()
        frontend.send_message(message.chat.id, t, reply_markup=m)
