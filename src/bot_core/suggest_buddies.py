from geopy.distance import distance
from data.user import User

eps = 5.0  # radius of our neighbourhood


# Метод должен возвращать список словарей, содержащих
# информацию о пользователях.
def suggest_buddies(user_id):
    other_buddies = list(User.select().where(User.id != user_id))
    our_buddy = User.get(User.id == user_id)
    our_location = (our_buddy.x, our_buddy.y)

    other_buddies_sorted = sorted(other_buddies, key=lambda buddy: distance(our_location, (buddy.x, buddy.y)).km)
    other_buddies_filtered = list(filter(lambda buddy: distance(our_location, (buddy.x, buddy.y)).km <= eps,
                                         other_buddies_sorted))
    return other_buddies_filtered
