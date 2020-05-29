from data.user import User
from data.activity import Activity


def get_user_by_id(user_id):
    query = User.select().where(User.id == user_id)
    return query


def user_exists(user_id):
    query = User.select().where(User.id == user_id)
    return query.exists()


def get_activities_by(user_id):
    return Activity.select().where(Activity.user_id == user_id)
