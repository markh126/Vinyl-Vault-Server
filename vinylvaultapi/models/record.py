from django.db import models
from .user import User
from .genre import Genre


class Record(models.Model):

    name = models.CharField(max_length=100)
    record_image_url = models.CharField(max_length=5000)
    artist = models.CharField(max_length=100)
    track_list = models.CharField(max_length=200)
    genre = models.ForeignKey(Genre, on_delete=models.DO_NOTHING)
    release_date = models.DateField()
    borrowed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)