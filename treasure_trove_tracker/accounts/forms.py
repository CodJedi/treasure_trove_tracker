from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import TreasuryUser


UserModel = get_user_model()

class TreasuryUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'password', 'password']

    def save(self, commit=True):
        user = super(TreasuryUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

# class TreasuryUserUpdateForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['email', 'password', 'password']
#
#     def save(self, commit=True):
#         user = super(TreasuryUserUpdateForm, self).save(commit=False)
#         user.email = self.cleaned_data['email']
#         if commit:
#             user.save()
#         return user

