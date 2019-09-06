# auto-generated snapshot
from peewee import *
import datetime
import peewee
import playhouse.postgres_ext


snapshot = Snapshot()


@snapshot.append
class Game(peewee.Model):
    title = CharField(max_length=100, unique=True)
    config = playhouse.postgres_ext.JSONField()
    class Meta:
        table_name = "game"


@snapshot.append
class User(peewee.Model):
    username = CharField(max_length=32, unique=True)
    password = CharField(max_length=255)
    class Meta:
        table_name = "user"


