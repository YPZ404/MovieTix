from django.db import models
from datetime import datetime

# Seat model
class Seat(models.Model):
    release_id = models.IntegerField()
    room_id = models.IntegerField()
    row_id = models.IntegerField()
    column_id = models.IntegerField()

    def toDict(self):
        return {'release_id': self.release_id, 'room_id': self.room_id, 'row_id': self.row_size, 'column_id': self.column_size,}

    class Meta:
        db_table = "Seat"


