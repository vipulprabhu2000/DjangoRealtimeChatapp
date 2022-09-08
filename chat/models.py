from django.db import models
from datetime import datetime

class room(models.Model):
    name=models.CharField(max_length=1000)

class messages(models.Model):
    roomid=models.CharField(max_length=1000)
    message=models.CharField(max_length=100000)
    date=models.DateTimeField(default=datetime.now,blank=True)
    user=models.CharField(max_length=1000)
