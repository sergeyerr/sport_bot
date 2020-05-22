from peewee import CharField, IntegerField, FloatField, Model
from data import database


class Activity(Model):
    id = IntegerField(primary_key=True)
    user_id = CharField()
    name = CharField()
    day = CharField()
    hours = CharField()
    x = FloatField()
    y = FloatField()

    class Meta:
        database = database
