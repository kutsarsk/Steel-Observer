from django.contrib.auth import models as auth_models, get_user_model
from django.db import models

from Steel_Observer.accounts.managers import AppUserManager


class AppUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):

    email = models.EmailField(null=False, blank=False, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    objects = AppUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


UserModel = get_user_model()


class Profile(models.Model):

    class Roles(models.TextChoices):
        ANALYST = 'Analyst', 'Analyst'
        BUSINESS_OWNER = 'Business owner', 'Business owner'
        BUYER = 'Buyer', 'Buyer'
        SELLER = 'Seller', 'Seller'
        UNKNOWN = 'Unknown', 'Unknown'

    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    role = models.CharField(max_length=30, choices=Roles.choices, default=Roles.UNKNOWN)

