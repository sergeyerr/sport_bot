from data.db import database
from data.user import User
from data.activity import Activity
from data.activities import Activities
from data.buddies import Buddies


def create_tables():
    with database:
        database.create_tables([User, Activity, Activities, Buddies])
