import peewee as pw
from data.db import database


class Activity(pw.Model):
    id = pw.IntegerField(primary_key=True)
    type = pw.CharField()
    distance = pw.DoubleField()
    date = pw.DateTimeField()
    x = pw.DoubleField()
    y = pw.DoubleField()

    class Meta:
        database = database
