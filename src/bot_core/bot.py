from data.user import User
from data.activity import Activity
from data.activities import Activities

def get_user_by_id(user_id):
    query = User.select().where(User.id == user_id)
    return query


def user_exists(user_id):
    query = User.select().where(User.id == user_id)
    return query.exists()


def get_activities_by(user_id):
    return Activity.select().where(Activity.user_id == user_id)


def save_user(new_user):
    fields = [User.id, User.name, User.username, User.age,
              User.gender, User.city, User.x, User.y]
    data = (new_user.id, new_user.name, new_user.username, new_user.age,
            new_user.gender, new_user.city, new_user.x, new_user.y)
    query = User.insert(data, fields=fields).execute()
    return query


#  для тестирования!! по факту надо учитывать user_id
def get_all_activities():
    return list(Activity.select())


def participate_in_activity(user_id, activity_id):
    Activities.insert(user_id=user_id, activity_id=activity_id).execute()


def quit_activity(user_id, activity_id):
    Activities.delete().where((Activities.activity_id == activity_id) & (Activities.user_id == user_id)).execute()


def is_participating(user_id, activity_id):
    return (Activities.select().where((Activities.activity_id == activity_id) & (Activities.user_id == user_id))).exists()
