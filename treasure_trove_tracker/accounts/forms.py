from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import TreasuryUser, Profile

UserModel = get_user_model()

class TreasuryUserCreationForm(auth_forms.UserCreationForm):
    user = None
    # password = forms.CharField(widget=forms.PasswordInput())
    class Meta(auth_forms.UserCreationForm.Meta):
        model = UserModel
        fields = ('email',)

    # def save(self, commit=True):
    #     user = super(TreasuryUserCreationForm, self).save(commit=False)
    #     user.set_password(self.cleaned_data["password"])
    #     if commit:
    #         user.save()
    #     return user

class TreasuryUserUpdateForm(auth_forms.UserChangeForm):
    # password = forms.CharField(widget=forms.PasswordInput(), required=False)
    class Meta(auth_forms.UserChangeForm.Meta):
        model = Profile
        fields = ('first_name', 'last_name', 'profile_pic', 'balance')

    # def save(self, commit=True):
    #     user = super(TreasuryUserUpdateForm, self).save(commit=False)
    #
    #     if self.cleaned_data['password']:
    #         user.set_password(self.cleaned_data['password'])
    #     if commit:
    #         user.save()
    #     return user

