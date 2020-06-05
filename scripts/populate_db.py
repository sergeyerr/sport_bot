from src.data.user import User
from src.data.activity import Activity
from src.data.activities import Activities
from src.data.buddies import Buddies


def insert_users():
    User.insert(id=0,
                name='Михаил',
                username='speedy_racer',
                age=99,
                gender='М',
                city='Пермь',
                x=58.01046,
                y=56.25017).execute()

    User.insert(id=1,
                name='Кирилл',
                username='white_lives_matter',
                age=9,
                gender='М',
                city='Миннеаполис',
                x=44.986656,
                y=-93.258133).execute()

    User.insert(id=2,
                name='Зоя',
                username='z1488',
                age=25,
                gender='F',
                city='Казань',
                x=55.78874,
                y=49.12214).execute()

    User.insert(id=3,
                name='Влад',
                username='vlad2007',
                age=13,
                gender='М',
                city='Владивосток',
                x=58.01046,
                y=56.25017).execute()

    User.insert(id=4,
                name='Дмитрий',
                username='dimon',
                age=30,
                gender='М',
                city='Москва',
                x=55.754093,
                y=37.620407).execute()

    User.insert(id=5,
                name='Сергей',
                username='data_scientist',
                age=10,
                gender='М',
                city='Калининград',
                x=54.70649,
                y=20.51095).execute()


def insert_activity():
    Activity.insert(id=0,
                    name='Марафон по ночной Перми',
                    type='Бег',
                    distance=5,
                    date='20201005 14:30:00',  # YYYYMMDD HH:MM:SS format
                    estimated_time='120',
                    x=58.21046,
                    y=56.35017).execute()

    Activity.insert(id=1,
                    name='Велозабег Пермь-Чернобыль',
                    type='Велогонка',
                    distance=1000,
                    date='20201115 15:00:00',
                    estimated_time='2000',
                    x=58.31046,
                    y=56.85017).execute()

    Activity.insert(id=2,
                    name='Спринт на стадионе Юность',
                    type='Бег',
                    distance=0.5,
                    date='20201202 18:00:00',
                    estimated_time='60',
                    x=59.01046,
                    y=53.25017).execute()

    Activity.insert(id=3,
                    name='Флексим на набережной',
                    type='Велопрогулка',
                    distance=2,
                    date='20200702 19:00:00',
                    estimated_time='80',
                    x=69.01046,
                    y=53.25017).execute()


def insert_activities():
    Activities.insert(activity_id=0,
                      user_id=0).execute()
    Activities.insert(activity_id=0,
                      user_id=3).execute()
    Activities.insert(activity_id=1,
                      user_id=2).execute()
    Activities.insert(activity_id=1,
                      user_id=3).execute()
    Activities.insert(activity_id=2,
                      user_id=0).execute()
    Activities.insert(activity_id=2,
                      user_id=1).execute()
    Activities.insert(activity_id=3,
                      user_id=0).execute()
    Activities.insert(activity_id=3,
                      user_id=4).execute()
    Activities.insert(activity_id=3,
                      user_id=5).execute()


def insert_buddies():
    Buddies.insert(buddy1=0, buddy2=1).execute()
    Buddies.insert(buddy1=0, buddy2=2).execute()
    Buddies.insert(buddy1=0, buddy2=3).execute()
    Buddies.insert(buddy1=0, buddy2=4).execute()
    Buddies.insert(buddy1=0, buddy2=5).execute()
    Buddies.insert(buddy1=1, buddy2=0).execute()
    Buddies.insert(buddy1=1, buddy2=5).execute()
    Buddies.insert(buddy1=3, buddy2=1).execute()
    Buddies.insert(buddy1=4, buddy2=2).execute()
    Buddies.insert(buddy1=5, buddy2=4).execute()
