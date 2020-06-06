from peewee import CharField, IntegerField, Model, DoubleField, DateTimeField, AutoField
from data.db import database


class Activity(Model):
    id = AutoField()
    name = CharField()
    type = CharField()
    distance = DoubleField()
    date = DateTimeField()
    estimated_time = IntegerField()  # в минутах
    x = DoubleField()
    y = DoubleField()

    class Meta:
        database = database
