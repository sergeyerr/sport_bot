from peewee import Model, CharField, IntegerField
from data import database


class User(Model):
    id = CharField(primary_key=True)
    link = CharField()
    name = CharField()
    age = IntegerField()
    gender = CharField()

    class Meta:
        database = database
