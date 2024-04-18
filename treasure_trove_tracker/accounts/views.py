from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views, login, logout, get_user_model
from django.urls import reverse_lazy
from django.views import generic as views

from treasure_trove_tracker.accounts.forms import TreasuryUserCreationForm, TreasuryUserUpdateForm
from treasure_trove_tracker.accounts.models import Profile
from treasure_trove_tracker.finance.models import Post

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
    template_name = 'accounts/profile_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Assuming 'profile_user' is the context variable for the User object
        context['posts'] = Post.objects.filter(author=self.request.user) # Get all posts by this user
        return context

class ProfileEditView(views.UpdateView):
    queryset = Profile.objects.all()
    template_name = 'accounts/profile_edit.html'
    form_class = TreasuryUserUpdateForm

    def get_success_url(self):
        return reverse_lazy(
            'user_profile_detail',
            kwargs={'pk': self.request.user.pk})

class ProfileDeleteView(views.DeleteView):
    queryset = Profile.objects.all()
    template_name = 'accounts/profile_delete.html'
    success_url = reverse_lazy('index')

