from geopy.distance import distance
from data.user import User
from data.activities import Activities
from data.activity import Activity


eps = 5.0  # radius of our neighbourhood


def suggest_activities(user_id):
    activity_ids = list(Activities.select().where(Activities.user_id == user_id))
    activities = list(Activity.select().where(Activity.id.not_in([act.activity_id for act in activity_ids])))
    our_buddy = User.get(User.id == user_id)
    our_location = (our_buddy.x, our_buddy.y)
    activities_filtered = list(filter(lambda act: distance(our_location, (act.x, act.y)).km <= eps,
                                      activities))
    activities_sorted = sorted(activities_filtered, key=lambda act: distance(our_location, (act.x, act.y)).km)
    return activities_sorted
