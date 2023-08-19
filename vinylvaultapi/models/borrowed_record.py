from django.db import models
from .user import User
from .record import Record

class BorrowedRecord(models.Model):

    record = models.ForeignKey(Record, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)