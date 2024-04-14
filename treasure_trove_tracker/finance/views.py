from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, TemplateView, CreateView

from .forms import TransactionForm
from .models import Transaction, Category, Trades, ProfitGoal

class DashboardView(LoginRequiredMixin, TemplateView):
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

class TransactionListView(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = 'finance/transaction_list.html'
    context_object_name = 'transactions'

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user).order_by('-date')

class TradesListView(LoginRequiredMixin, ListView):
    model = Trades
    template_name = 'finance/trades_list.html'
    context_object_name = 'trades'

    def get_queryset(self):
        return Trades.objects.filter(user=self.request.user).order_by('-purchase_date')

class CreateTransactionView(LoginRequiredMixin, CreateView):
    model = Transaction
    form_class = TransactionForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)