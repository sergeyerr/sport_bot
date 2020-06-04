from peewee import IntegerField, Model, CompositeKey
from data.db import database


class Buddies(Model):
    buddy1 = IntegerField()
    buddy2 = IntegerField()

    class Meta:
        database = database
        primary_key = CompositeKey('buddy1', 'buddy2')
