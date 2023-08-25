from django.db import models
from .user import User
from .record import Record

class WishlistRecord(models.Model):

    record = models.ForeignKey(Record, on_delete=models.CASCADE, related_name='record')
    user = models.ForeignKey(User, on_delete=models.CASCADE)