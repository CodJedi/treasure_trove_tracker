from django.contrib import admin
from django.urls import path, include
from treasure_trove_tracker.finance.views import DashboardView, TransactionListView, TradesListView, \
    CreateTransactionView, PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, ContactFormView

urlpatterns = [
    path('', include([
         path('dashboard/', DashboardView.as_view(), name='dashboard'),
         path('transactions/', TransactionListView.as_view(), name='transactions'),
         path('trades/', TradesListView.as_view(), name='trades'),
         path('create_transaction/', CreateTransactionView.as_view(), name='create_transaction'),
    ])
         ),
    path('blog/',PostListView.as_view(), name='blog',),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('post/', include([
        path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
        path('create/', PostCreateView.as_view(), name='post_create'),
        path('<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
        path('<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
])
         ),
]
