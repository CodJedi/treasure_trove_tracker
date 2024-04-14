
from django.urls import path, include
from treasure_trove_tracker.core.views import IndexView

urlpatterns = (
    path('', IndexView.as_view(), name='index'),
)
