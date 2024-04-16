from django.shortcuts import render
from django.contrib.auth import mixins as auth_mixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic as views
from .forms import TransactionForm, PostForm
from .models import Transaction, Category, Trades, ProfitGoal, Post
from ..core.view_mixins import OwnerRequiredMixin


class PostCreateView(LoginRequiredMixin, views.CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_create.html'
    success_url = reverse_lazy('blog')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostListView(auth_mixin.LoginRequiredMixin, views.ListView):
    model = Post
    template_name = 'blog/blog.html'


class PostDetailView(auth_mixin.LoginRequiredMixin, views.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'



class PostUpdateView(OwnerRequiredMixin,auth_mixin.LoginRequiredMixin, views.UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_edit.html'
    success_url = reverse_lazy('blog')

    def get_queryset(self):
        """ Restrict users to only modify their own posts. """
        return super().get_queryset().filter(author=self.request.user)


class PostDeleteView(OwnerRequiredMixin,auth_mixin.LoginRequiredMixin, views.DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('blog')


# Finance part of the project
class DashboardView(LoginRequiredMixin, views.TemplateView):
    template_name = 'finance/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context = {
            'transactions': Transaction.objects.filter(user=user).order_by('-date')[:5],
            'trades': Trades.objects.filter(user=user).order_by('-purchase_date')[:5],
            'profit_goals': ProfitGoal.objects.filter(user=user),
        }
        return context


class TransactionListView(LoginRequiredMixin, views.ListView):
    model = Transaction
    template_name = 'finance/transaction_list.html'
    context_object_name = 'transactions'

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user).order_by('-date')


class TradesListView(LoginRequiredMixin, views.ListView):
    model = Trades
    template_name = 'finance/trades_list.html'
    context_object_name = 'trades'

    def get_queryset(self):
        return Trades.objects.filter(user=self.request.user).order_by('-purchase_date')


class CreateTransactionView(LoginRequiredMixin, views.CreateView):
    model = Transaction
    form_class = TransactionForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
