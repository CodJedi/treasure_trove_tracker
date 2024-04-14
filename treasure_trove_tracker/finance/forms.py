from django import forms
from .models import Transaction, Category, Trades, ProfitGoal

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = [
            'description',
            'amount',
            'transaction_type',
        ]

class TradesForm(forms.ModelForm):
    class Meta:
        model = Trades
        fields = [
            'asset_name',
            'purchase_price',
            'current_price',
            'quantity',

        ]

class ProfitGoalForm(forms.ModelForm):
    class Meta:
        model = ProfitGoal
        fields = [
            'target_amount',

        ]
