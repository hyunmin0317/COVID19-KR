from django.db import models


# Create your models here.

class Data(models.Model):
    date = models.DateTimeField()
    confirmed = models.IntegerField()
    death = models.IntegerField()
    released = models.IntegerField()
    tested = models.IntegerField()
    today = models.IntegerField()

    def __str__(self):
        return self.date.strftime('%Y-%m-%d')