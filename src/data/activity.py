from peewee import CharField, IntegerField, Model, DoubleField, DateTimeField
from data.db import database


class Activity(Model):
    id = IntegerField(primary_key=True)
    type = CharField()
    distance = DoubleField()
    date = DateTimeField()
    x = DoubleField()
    y = DoubleField()

    class Meta:
        database = database
