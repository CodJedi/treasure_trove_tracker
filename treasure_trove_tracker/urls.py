
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('treasure_trove_tracker.accounts.urls')),
    path('', include('treasure_trove_tracker.core.urls')),
    path('accounts/', include('treasure_trove_tracker.accounts.urls')),
    path('finance/', include('treasure_trove_tracker.finance.urls')),

]
