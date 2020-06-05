from peewee import CharField, IntegerField, Model, DoubleField, DateTimeField
from data.db import database


class Activity(Model):
    id = IntegerField(primary_key=True)
    name = CharField()
    type = CharField()
    distance = DoubleField()
    date = DateTimeField()
    estimated_time = IntegerField()  # в минутах
    x = DoubleField()
    y = DoubleField()

    class Meta:
        database = database
