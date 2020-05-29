import peewee as pw
from data.db import database


class User(pw.Model):
    id = pw.IntegerField(primary_key=True)
    name = pw.CharField()
    username = pw.CharField()
    age = pw.IntegerField()
    city = pw.CharField()
    x = pw.DoubleField()
    y = pw.DoubleField()

    class Meta:
        database = database
