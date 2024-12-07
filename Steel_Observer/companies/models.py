from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class Company(models.Model):

    class BusinessFields(models.TextChoices):
        CONSTRUCTION = 'Construction', 'Construction'
        ENGINEERING = 'Engineering', 'Engineering'
        MACHINE_BUILDING = 'Machine building', 'Machine building'
        SHIPBUILDING = 'Shipbuilding', 'Shipbuilding'
        STEEL_PRODUCTION = 'Steel production', 'Steel production'
        STEEL_TRADE = 'Steel trade', 'Steel trade'
        UNKNOWN = 'Unknown', 'Unknown'

    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    business_field = models.CharField(max_length=50, choices=BusinessFields.choices, default=BusinessFields.UNKNOWN)
    products = models.TextField(null=True, blank=True)
    user = models.ForeignKey(to=UserModel, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name
