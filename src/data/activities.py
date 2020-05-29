import peewee as pw
from data.db import database


class Activities(pw.Model):
    activity_id = pw.IntegerField()
    user_id = pw.IntegerField()

    class Meta:
        database = database
        primary_key = pw.CompositeKey('activity_id', 'user_id')
