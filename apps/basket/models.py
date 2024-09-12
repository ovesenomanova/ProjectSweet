from django.db import models
from django.contrib.auth import get_user_model
from apps.catalog.models import Catalog

class Basket (models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    cake = models.ForeignKey(Catalog, on_delete=models.CASCADE)




