from sys import argv

from data import db, activities, activity, user
from frontend.ui_components import main_menu, stats_display
from frontend import util
from frontend import setup

if len(argv) == 2:
    setup.create_frontend(argv[1])
