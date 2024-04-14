from django.db import models
from django.conf import settings


class Transaction(models.Model):
    TRANSACTION_TYPE_CHOICES = [
        ('income', 'Income'),
        ('expense', 'Expense'),
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
        default='expense'
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
