from django.db import models
from django.conf import settings
from django.utils.text import slugify


class Post(models.Model):
    title = models.CharField(
        max_length=200
    )
    content = models.TextField(
        blank=True,
    )
    text = models.TextField(
        blank=True,
        null=True,
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='posts',
    )
    created_date = models.DateTimeField(
        auto_now_add=True,
    )
    image = models.URLField(
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    author = models.CharField(
        max_length=50
    )
    text = models.TextField(
        blank=True,
        null=True,
        max_length=1000
    )
    created_date = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return self.text

# Finance part of the project
class Transaction(models.Model):
    TRANSACTION_TYPE_CHOICES = [
        ('trades', 'Trades'),
    ]
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    description = models.CharField(
        max_length=1000,
        blank=True,
    )
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    date = models.DateField(
        auto_now_add=True
    )
    transaction_type = models.CharField(
        max_length=10,
        choices=TRANSACTION_TYPE_CHOICES,
        default='trades'
    )

    def __str__(self):
        return f"{self.transaction_type} - {self.amount} on {self.date}"


class Category(models.Model):
    name = models.CharField(
        max_length=100,
    ),
    transaction_type = models.CharField(
        max_length=10,
        choices=Transaction.TRANSACTION_TYPE_CHOICES,
    )


class Trades(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    asset_name = models.CharField(
        max_length=100
    )
    purchase_price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    current_price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    quantity = models.DecimalField(
        max_digits=10,
        decimal_places=3
    )
    purchase_date = models.DateField(
        auto_now_add=True
    )


class ProfitGoal(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    target_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )
    current_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )
    description = models.CharField(
        max_length=1000,
    )

class ContactEmailMessage(models.Model):
    theme = models.CharField(
        max_length=255,
        blank=False,
        null=False,
    )
    email = models.EmailField(
        max_length=255,
        blank=False,
        null=False,
    )
    message = models.TextField(
        max_length=1000,
        blank=False,
        null=False,

    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return f"Email: {self.theme} from {self.email}"