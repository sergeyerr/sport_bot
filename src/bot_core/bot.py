from geopy.distance import distance
from data.user import User
from data.activities import Activities
from data.activity import Activity
from data.buddies import Buddies
from peewee import SQL, fn


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
    return new_user.save()


def user_distance(user_a, user_b):
    return distance((user_a.x, user_a.y), (user_b.x, user_b.y)).km


def create_activity(a: Activity):
    na = Activity.create(
        name=a.name,
        x=a.x, y=a.y,
        date=a.date,
        distance=a.distance,
        estimated_time=a.estimated_time,
        type=a.type)

    return na.save()


def buddies_by_user_id(user_id:int) -> list:
    """
    возвращает друзей пользователя
    :param user_id: int ID в телеграма
    :return: list
    """
    Buddy = User.alias()
    return list(User
     .select()
     .join(Buddies, on=(Buddies.buddy2 == User.id))
     .join(Buddy, on=(Buddies.buddy1 == Buddy.id))
     .where(Buddy.id == user_id))


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


def bud(buddy_a, buddy_b_id):
    Buddies.insert(buddy1=buddy_a, buddy2=buddy_b_id).execute()


def unbud(buddy_a_id, buddy_b_id):
    Buddies.delete().where(
        (Buddies.buddy1 == buddy_a_id)
        & (Buddies.buddy2 == buddy_b_id)
    ).execute()


def one_way_buddies(user_a_id, user_b_id):
    return Buddies.select().where(
        (Buddies.buddy1 == user_a_id)
        & (Buddies.buddy2 == user_b_id)
    ).exists()


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


def get_top_user_activity(user_id: int) -> list:
    """
    возвращает самую популярную активность пользователя
    :param user_id: int ID в телеграма
    :return: list
    """
    return list(Activity.select(fn.COUNT(Activity.id).alias('totalcount'), Activity.type)
                .join(Activities).join(User)
                .where(User.id == user_id)
                .group_by(Activity.type)
                .order_by(SQL('totalcount').desc()))


def get_finished_user_activities(user_id: int) -> list:
    """
    возвращает кол-во завершённых активностей
    :param user_id: int ID в телеграма
    :return: list
    """
    return list(User.select(fn.COUNT(Activity.id).alias('totalcount')) \
                .join(Activities).join(Activity) \
                .where(User.id == user_id) \
                .group_by(User.id))


def get_top_by_activity(activity: str) -> list:
    """
    возвращает кол-во завершённых активностей по ТИПУ активности
    :param activity: str ID в телеграма
    :return: list
    """
    return list(User.select(fn.COUNT(Activity.id).alias('totalcount'), User.username)
                .join(Activities).join(Activity)
                .group_by(User.username)
                .order_by(SQL('totalcount').desc()))
