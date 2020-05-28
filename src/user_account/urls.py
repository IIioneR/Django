from django.conf import settings
from django.urls import include
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from user_account.views import CreateUserAccountView

urlpatterns = [
    path('register/', CreateUserAccountView.as_view(), name='registration'),
    path('successfully/', TemplateView.as_view(template_name='successfully.html'), name='successfully'),
]
