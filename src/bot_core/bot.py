from geopy.distance import distance
from data.user import User
from data.activities import Activities
from data.activity import Activity
from data.buddies import Buddies


def get_user_by_id(user_id):
    try:
        return User.get(User.id == user_id)
    except Exception:
        return None


def user_exists(user_id):
    try:
        User.get(User.id == user_id)
        return True
    except Exception:
        return False


def create_user(new_user):
    return new_user.save(force_insert=True)


def create_activity(new_activity):
    return new_activity.save(force_insert=True)


def buddies_by_user_id(user_id):
    return []


def suggest_activities(user_id, radius=30.0):
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


def suggest_buddies(user_id, radius=30.0):
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


#  для тестирования!! по факту надо учитывать user_id
def get_all_activities():
    return list(Activity.select())


def activities_by_user(user_id):
    return list(
        Activity
        .select()
        .join(Activities)
        .join(User)
        .where(User.id == user_id))


def users_by_activity(activity_id):
    return list(
        User
        .select()
        .join(Activities)
        .join(Activity)
        .where(Activity.id == activity_id)
    )


def participate_in_activity(user_id, activity_id):
    Activities.insert(user_id=user_id, activity_id=activity_id).execute()


def quit_activity(user_id, activity_id):
    Activities.delete().where(
        (Activities.activity_id == activity_id)
        & (Activities.user_id == user_id)
    ).execute()


def is_participating(user_id, activity_id):
    return Activities.select().where(
        (Activities.activity_id == activity_id)
        & (Activities.user_id == user_id)
    ).exists()
