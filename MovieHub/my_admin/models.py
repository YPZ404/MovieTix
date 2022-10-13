from django.db import models
from datetime import datetime


# Staff Model
class Staff(models.Model):
    staff_id = models.IntegerField()
    password_hash = models.CharField(max_length=100)
    password_salt = models.CharField(max_length=50)
    name = models.CharField(max_length=20)
    level = models.IntegerField(default=0)  # level 0: normal 1:manager
    phone = models.IntegerField()
    email = models.CharField(max_length=40)
    create_time = models.DateTimeField(default=datetime.now)
    update_time = models.DateTimeField(default=datetime.now)

    def toDict(self):
        return {'staff_id': self.staff_id, 'password_hash': self.password_hash, 'password_salt': self.password_salt,
                'name': self.name, 'level': self.level, 'phone': self.phone, 'email': self.email,
                'create_time': self.create_time.strftime('%Y-%m-%d %H:%M:%S'),
                'update_time': self.update_time.strftime('%Y-%m-%d %H:%M:%S')}

    class Meta:
        db_table = "Staff"


# Room Model
class Room(models.Model):
    room_id = models.IntegerField()
    row_size = models.IntegerField()
    column_size = models.IntegerField()
    create_time = models.DateTimeField(default=datetime.now)
    update_time = models.DateTimeField(default=datetime.now)

    def toDict(self):
        return {'room_id': self.room_id, 'row_size': self.row_size, 'column_size': self.column_size,
                'total_size': self.row_size * self.column_size,
                'create_time': self.create_time.strftime('%Y-%m-%d %H:%M:%S'),
                'update_time': self.update_time.strftime('%Y-%m-%d %H:%M:%S')}

    class Meta:
        db_table = "Room"


# Movie Model
class Movie(models.Model):
    movie_id = models.IntegerField()
    movie_name = models.CharField(max_length=40)
    poster = models.CharField(max_length=255)
    type = models.CharField(max_length=20)
    cast = models.CharField(max_length=100)
    introduction = models.CharField(max_length=100)
    create_time = models.DateTimeField(default=datetime.now)
    update_time = models.DateTimeField(default=datetime.now)

    def toDict(self):
        return {'movie_id': self.movie_id, 'movie_name': self.movie_name, 'poster': self.poster,
                'type': self.type, 'cast': self.cast, 'introduction': self.introduction,
                'create_time': self.create_time.strftime('%Y-%m-%d %H:%M:%S'),
                'update_time': self.update_time.strftime('%Y-%m-%d %H:%M:%S')}

    class Meta:
        db_table = "Movie"


class Announcement(models.Model):
    announcement_id = models.IntegerField()
    content = models.CharField(max_length=255)
    create_time = models.DateTimeField(default=datetime.now)
    update_time = models.DateTimeField(default=datetime.now)

    def toDict(self):
        return {'announcement_id': self.announcement_id, 'content': self.content,
                'create_time': self.create_time.strftime('%Y-%m-%d %H:%M:%S'),
                'update_time': self.update_time.strftime('%Y-%m-%d %H:%M:%S')}

    class Meta:
        db_table = "Announcement"
