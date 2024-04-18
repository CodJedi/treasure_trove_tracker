from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field
from django import forms
from .models import Transaction, Category, Trades, ProfitGoal, Post, Comment, ContactEmailMessage


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'image',
        ]
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        labels = {
            'text': 'Join the conversation',
        }
        widgets = {
            'text': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }

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

# forms.py
class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactEmailMessage
        fields = ['theme', 'email', 'message']


