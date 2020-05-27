from peewee import Model, CharField, IntegerField, DoubleField
from data.db import database


class User(Model):
    id = IntegerField(primary_key=True)
    name = CharField()
    login = CharField()
    age = IntegerField()
    city = CharField()
    x = DoubleField()
    y = DoubleField()

    class Meta:
        database = database
