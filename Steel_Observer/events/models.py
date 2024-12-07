from django.contrib.auth import get_user_model
from django.db import models

from Steel_Observer.companies.models import Company
from Steel_Observer.products.models import Product

UserModel = get_user_model()


class Event(models.Model):

    name = models.CharField(max_length=50)
    date = models.DateField()
    place = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    user = models.ForeignKey(to=UserModel, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name

