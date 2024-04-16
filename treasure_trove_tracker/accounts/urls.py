
from django.urls import path, include
from treasure_trove_tracker.accounts.views import LoginUserView, user_logout, SignupUserView, ProfileEditView, \
    ProfileDeleteView, ProfileDetailView

urlpatterns = (
    path('login/', LoginUserView.as_view(), name='user_login'),
    path('logout/', user_logout, name='user_logout'),
    path('signup/', SignupUserView.as_view(), name='user_signup'),
    path(
        'profile/<int:pk>/', include([
            path('', ProfileDetailView.as_view(), name='user_profile_detail'),
            path('edit/', ProfileEditView.as_view(), name='user_profile_edit'),
            path('delete/', ProfileDeleteView.as_view(), name='user_profile_delete'),
        ]),
    ),
)
