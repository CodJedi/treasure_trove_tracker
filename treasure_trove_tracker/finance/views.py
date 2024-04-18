from django.shortcuts import render, redirect
from django.contrib.auth import mixins as auth_mixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views import generic as views
from django.contrib import messages

from .forms import TransactionForm, PostForm, CommentForm, ContactForm
from .models import Transaction, Category, Trades, ProfitGoal, Post, Comment
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = context['post']
        comments = Comment.objects.filter(post=post)
        context['comments'] = comments
        context['comment_form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = self.object
            comment.author = request.user
            comment.save()
            return redirect(reverse('post_detail', kwargs={'pk': self.object.pk}))
        return self.get(request, *args, **kwargs, comment_form=comment_form)


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

class ContactFormView(LoginRequiredMixin,views.FormView):
    form_class = ContactForm
    template_name = 'finance/contact.html'
    success_url = reverse_lazy('contact')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Your message has been sent!')
        return super().form_valid(form)

# def contact_view(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Your message has been sent!')
#             return redirect(reverse('contact'))
#     else:
#         form = ContactForm()
#
#     return render(request, 'finance/contact.html', {'form': form})