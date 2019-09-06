# auto-generated snapshot
from peewee import *
import datetime
import peewee
import playhouse.postgres_ext


snapshot = Snapshot()


@snapshot.append
class Game(peewee.Model):
    title = CharField(max_length=100)
    config = playhouse.postgres_ext.JSONField()
    class Meta:
        table_name = "game"


