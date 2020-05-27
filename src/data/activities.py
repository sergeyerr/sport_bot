from peewee import CharField, IntegerField, Model, DoubleField, DateTimeField, CompositeKey
from data.db import database


class Activities(Model):
    activity_id = IntegerField()
    user_id = IntegerField()

    class Meta:
        database = database
        primary_key = CompositeKey('activity_id','user_id')
