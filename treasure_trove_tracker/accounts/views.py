from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views, login, logout, get_user_model
from django.urls import reverse_lazy
from django.views import generic as views

from treasure_trove_tracker.accounts.forms import TreasuryUserCreationForm

UserModel = get_user_model()
class LoginUserView(auth_views.LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True

class SignupUserView(views.CreateView):
    form_class = TreasuryUserCreationForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, form.instance)
        return result

def user_logout(request):
    logout(request)
    return redirect('index')

class ProfileDetailView(views.DetailView):
    model = UserModel
    template_name = 'accounts/profile.html'

class ProfileEditView(views.UpdateView):
    model = UserModel
    template_name = 'accounts/profile_edit.html'
    fields = ['first_name', 'last_name', 'email']
    success_url = reverse_lazy('profile_detail')

    def get_object(self):
        return self.request.user

class ProfileDeleteView(views.DeleteView):
    model = UserModel
    template_name = 'accounts/profile_delete.html'
    success_url = reverse_lazy('index')

