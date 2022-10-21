from django.db import models

# Create your models here.
class Movie(models.Model):
    movie_id = models.IntegerField(unique=True)
    movie_name = models.CharField(max_length=40)
    poster = models.CharField(max_length=255)
    type = models.CharField(max_length=20)
    cast = models.CharField(max_length=100, blank=True, null=True)
    introduction = models.CharField(max_length=100, blank=True, null=True)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()

    class Meta:
        db_table = 'movie'
     
class Release(models.Model):
    release_id = models.IntegerField(unique=True)
    movie_id = models.IntegerField()
    room_id = models.IntegerField()
    release_time = models.DateTimeField()
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()

    class Meta:
        db_table = 'release'