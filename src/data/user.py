from peewee import Model, CharField, IntegerField, DoubleField
from data.db import database


class User(Model):
    id = IntegerField(primary_key=True)
    name = CharField()
    username = CharField()
    age = IntegerField()
    gender = CharField()
    city = CharField()
    x = DoubleField()
    y = DoubleField()

    class Meta:
        database = database
