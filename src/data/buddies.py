from peewee import IntegerField, Model, CompositeKey, ForeignKeyField
from data.db import database
from data.user import User


class Buddies(Model):
    buddy1 = ForeignKeyField(User, to_field="id")
    buddy2 = ForeignKeyField(User, to_field="id")

    class Meta:
        database = database
        primary_key = CompositeKey('buddy1', 'buddy2')
