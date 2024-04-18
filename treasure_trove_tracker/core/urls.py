
from django.urls import path, include
from treasure_trove_tracker.core.views import IndexView, AboutView,FAQView

urlpatterns = (
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('faq/', FAQView.as_view(), name='faq'),
    )
