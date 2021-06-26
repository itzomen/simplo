from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
from versatileimagefield.fields import VersatileImageField
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import UserManager

from .validators import validate_possible_number


class PossiblePhoneNumberField(PhoneNumberField):
    """Less strict field for phone numbers written to database."""

    default_validators = [validate_possible_number]


class User(AbstractBaseUser, PermissionsMixin):
    # base models
    email = models.EmailField(unique=True, null=True, db_index=True)
    first_name = models.CharField(max_length=250, blank=True)
    last_name = models.CharField(max_length=250, blank=True)

    # profile
    avatar = VersatileImageField(upload_to="user-avatars", blank=True, null=True)
    phone = PossiblePhoneNumberField(blank=True, default="")

    # fields for management
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now, editable=False)

    USERNAME_FIELD = "email"

    objects = UserManager()

    class Meta:
        ordering = ("email",)

    def __str__(self):
        return f"{self.email} - {self.first_name} {self.last_name}"
