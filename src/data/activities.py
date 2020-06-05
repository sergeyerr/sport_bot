from peewee import IntegerField, Model, CompositeKey, ForeignKeyField
from data.db import database
from data.activity import Activity
from data.user import User


class Activities(Model):
    activity_id = ForeignKeyField(Activity, to_field="id")
    user_id = ForeignKeyField(User, to_field="id")

    class Meta:
        database = database
        primary_key = CompositeKey('activity_id', 'user_id')
