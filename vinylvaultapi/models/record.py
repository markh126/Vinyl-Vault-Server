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
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    @property
    def wishlisted(self):
        """Custom property that shows if a record is wishlisted"""
        return self.__wishlisted

    @wishlisted.setter
    def wishlisted(self, value):
        self.__wishlisted = value

    @property
    def borrowed(self):
        """Custom property that shows if a record has been borrowed"""
        return self.__borrowed

    @borrowed.setter
    def borrowed(self, value):
        self.__borrowed = value