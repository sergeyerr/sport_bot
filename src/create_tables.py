from src.data.db import database
from src.data.user import User
from src.data.activity import Activity
from src.data.activities import Activities
from src.data.buddies import Buddies

#from scripts.populate_db import insert_users, insert_activity, insert_activities, insert_buddies

with database:
    database.create_tables([User, Activity])
    database.create_tables([Activities, Buddies])

#insert_users()
#insert_activity()
#insert_activities()
#insert_buddies()


