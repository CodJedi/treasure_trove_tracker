from django.contrib import admin
from django.urls import path, include
from treasure_trove_tracker.finance.views import DashboardView, TransactionListView, TradesListView, CreateTransactionView


urlpatterns = [
    path('finance/', include([
         path('dashboard/', DashboardView.as_view(), name='dashboard'),
         path('transactions/', TransactionListView.as_view(), name='transactions'),
         path('trades/', TradesListView.as_view(), name='trades'),
         path('create_transaction/', CreateTransactionView.as_view(), name='create_transaction'),
    ])
         ),
]
