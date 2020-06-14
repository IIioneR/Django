from django.conf import settings
from django.urls import include
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from user_account.views import CreateUserAccountView, UserAccountLoginView, UserAccountLogoutView, \
    UserAccountUpdateView, user_account_profile

urlpatterns = [
    path('register/', CreateUserAccountView.as_view(), name='registration'),
    path('success-page/', TemplateView.as_view(template_name='successfully.html'), name='successfully'),
    path('login/', UserAccountLoginView.as_view(), name='login'),
    path('logout/', UserAccountLogoutView.as_view(), name='logout'),
    path('profile/', user_account_profile, name='profile'),
]
