from django.db import models


class Catalog(models.Model):
    content = models.CharField(max_length=256)

