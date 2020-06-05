from data.db import database
from data.user import User
from data.activity import Activity
from data.activities import Activities
from data.buddies import Buddies

from scripts.populate_db import insert_users, insert_activity, insert_activities, insert_buddies

with database:
    database.create_tables([User, Activity, Activities, Buddies])

insert_users()
insert_activity()
insert_activities()
insert_buddies()


