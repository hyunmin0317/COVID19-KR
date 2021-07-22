from django.db import models

# Create your models here.

class Covid19():
    def __init__(self, d, c, de, r, t, to):
        self.date = d
        self.confirmed = c
        self.death = de
        self.released = r
        self.tested = t
        self.today = to
