from django.db import models
from _datetime import datetime
from django.utils.timesince import timesince


# Create your models here.


class Blogs(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=50)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title

    def get_time_diff(self):
        return timesince(self.date, datetime.now().date())
