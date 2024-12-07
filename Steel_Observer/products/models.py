from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class Product(models.Model):

    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(null=True, blank=True)
    user = models.ForeignKey(to=UserModel, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name
