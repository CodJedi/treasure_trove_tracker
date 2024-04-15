from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views, login, logout, get_user_model
from django.urls import reverse_lazy
from django.views import generic as views

from treasure_trove_tracker.accounts.forms import TreasuryUserCreationForm
from treasure_trove_tracker.accounts.models import Profile

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
    queryset = Profile.objects.prefetch_related('user').all()
    template_name = 'accounts/profile.html'

class ProfileEditView(views.UpdateView):
    queryset = Profile.objects.all()
    template_name = 'accounts/profile_edit.html'
    success_url = reverse_lazy('profile_detail')

    def get_object(self):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy(
            'profile_detail',
            kwargs={'pk': self.request.user.pk})

class ProfileDeleteView(views.DeleteView):
    queryset = Profile.objects.all()
    template_name = 'accounts/profile_delete.html'
    success_url = reverse_lazy('index')

