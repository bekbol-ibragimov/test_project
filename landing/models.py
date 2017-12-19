from django.db import models

class Subscriber(models.Model):
    emeil = models.EmailField()
    name = models.CharField(max_length=128)