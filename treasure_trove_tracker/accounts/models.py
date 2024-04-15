from django.conf import settings
from django.db import models
from django.contrib.auth import models as auth_models
from django.utils.translation import gettext_lazy as _

from treasure_trove_tracker.accounts.managers import TreasuryUserManager


class TreasuryUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    email = models.EmailField(
        _('email address'),
        unique=True,
        error_messages={
            "unique": "A user with that email already exists."
        },
    )
    first_name = models.CharField(
        _('first name'),
        max_length=30,
    )
    last_name = models.CharField(
        _('last name'),
        max_length=30,
    )
    is_staff = models.BooleanField(
        default=False
    )
    is_active = models.BooleanField(
        default=True,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = TreasuryUserManager()

class Profile(models.Model):
    user = models.OneToOneField(
        TreasuryUser,
        on_delete=models.CASCADE,
        related_name="profile",
    )

    balance = models.DecimalField(
        default=0,
        max_digits=10,
        decimal_places=2,
    )

    first_name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    last_name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    profile_pic = models.URLField(
        blank=True,
        null=True,
    )

    @property
    def full_name(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        else:
            return self.first_name or self.last_name


