from django.db import models


class Payment(models.Model):
    name = models.CharField(max_length=256)
    foto = models.CharField(max_length=256)
    description = models.CharField(max_length=256)
    price = models.CharField(max_length=256)