from django.db import models
from django.contrib.auth.models import AbstractUser

class TreasuryUser(AbstractUser):
    email = models.EmailField(
        unique=True,
        error_messages={
            "unique": "A user with that email already exists."
        },
    )
    is_staff = models.BooleanField(
        default=False
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'username',
    ]

class Profile(models.Model):
    user = models.OneToOneField(
        TreasuryUser,
        on_delete=models.CASCADE)

    balance = models.DecimalField(
        default=0),

    first_name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    ),
    last_name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    ),

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    ),

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


