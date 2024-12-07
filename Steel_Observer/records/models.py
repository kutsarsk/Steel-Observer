from django.contrib.auth import get_user_model
from django.db import models

from Steel_Observer.products.models import Product

UserModel = get_user_model()


class Record(models.Model):

    class TransactionTypes (models.TextChoices):
        BID = 'Bid', 'Bid'
        OFFER = 'Offer', 'Offer'
        DEAL = 'Deal', 'Deal'

    class Currencies (models.TextChoices):
        USD = 'USD', 'USD'
        EUR = 'EUR', 'EUR'

    class Regions (models.TextChoices):
        BALKANS = 'Balkans', 'Balkans'
        CENTRAL_EUROPE = 'Central Europe', 'Central Europe'
        EASTERN_EUROPE = 'Eastern Europe', 'Eastern Europe'
        NORTHERN_EUROPE = 'Northern Europe', 'Northern Europe'
        SOUTHERN_EUROPE = 'Southern Europe', 'Southern Europe'
        TURKEY = 'Turkey', 'Turkey'
        CHINA = 'China', 'China'
        EAST_ASIA = 'East Asia', 'East Asia'
        SOUTH_ASIA = 'South Asia', 'South Asia'
        OTHER = 'Other', 'Other'

    date = models.DateField(auto_now_add=True)
    region = models.CharField(max_length=50, choices=Regions.choices, default=Regions.OTHER)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    currency = models.CharField(choices=Currencies.choices, default=Currencies.USD, max_length=5)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(choices=TransactionTypes.choices, default=TransactionTypes.OFFER, max_length=10)
    user = models.ForeignKey(to=UserModel, on_delete=models.CASCADE, default=1)

    def __str__(self):

        transaction_type = '? at'

        if self.type == self.TransactionTypes.BID:
            transaction_type = 'wanted at'
        elif self.type == self.TransactionTypes.OFFER:
            transaction_type = 'offered at'
        elif self.type == self.TransactionTypes.DEAL:
            transaction_type = 'sold at'

        return f'{self.date} -- {self.product} {transaction_type} {self.price:.2f} {self.currency}'
