from geopy.distance import distance
from data.user import User
from data.activities import Activities
from data.activity import Activity

def get_user_by_id(user_id):
    try:
        return User.get(User.id == user_id)
    except Exception:
        return None


def user_exists(user_id):
    try:
        print(user_id)
        User.get(User.id == user_id)
        print("TRUE")
        return True
    except Exception:
        return False


def get_activities_by(user_id):
    return Activity.select().where(Activity.user_id == user_id)


def create_user(new_user):
    # fields = [User.id, User.name, User.username, User.age,
    #           User.gender, User.city, User.x, User.y]
    # data = (new_user.id, new_user.name, new_user.username, new_user.age,
    #         new_user.gender, new_user.city, new_user.x, new_user.y)
    # query = User.insert(data, fields=fields).execute()
    # return query
    return new_user.save(force_insert=True)


def create_activity(new_activity):
    # fields = [Activity.type, Activity.distance, Activity.date,
    #           Activity.x, Activity.y]
    # data = (new_activity.type, new_activity.distance,
    #         new_activity.date, new_activity.x, new_activity.y)
    # query = Activity.insert(data, fields=fields).execute()
    # return query
    return new_activity.save(force_insert=True)


def suggest_activities(user_id, radius=5.0):
    """
        Находит мероприятия в округе
    """

    activity_ids = list(Activities.select().where(
        Activities.user_id == user_id))
    activities = list(Activity.select().where(
        Activity.id.not_in([act.activity_id for act in activity_ids])))
    our_buddy = User.get(User.id == user_id)
    our_location = (our_buddy.x, our_buddy.y)
    activities_filtered = list(filter(
        lambda act: distance(our_location, (act.x, act.y)).km <= radius,
        activities))
    activities_sorted = sorted(
        activities_filtered,
        key=lambda act: distance(our_location, (act.x, act.y)).km)

    return activities_sorted


def suggest_buddies(user_id, radius):
    """
        Находит пользователей в округе
    """

    other_buddies = list(User.select().where(User.id != user_id))
    our_buddy = User.get(User.id == user_id)
    our_location = (our_buddy.x, our_buddy.y)

    other_buddies_sorted = sorted(
        other_buddies,
        key=lambda buddy: distance(our_location, (buddy.x, buddy.y)).km)
    other_buddies_filtered = list(filter(
        lambda buddy: distance(our_location, (buddy.x, buddy.y)).km <= radius,
        other_buddies_sorted))

    return other_buddies_filtered
