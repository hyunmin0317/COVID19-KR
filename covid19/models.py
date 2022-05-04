from django.db import models

class Data(models.Model):
    date = models.CharField(max_length=10, unique=True)
    confirmed = models.CharField(max_length=50)
    death = models.CharField(max_length=50)
    today_confirmed = models.CharField(max_length=50)
    today_death = models.CharField(max_length=50)

    def __str__(self):
        return self.date