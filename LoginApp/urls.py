from django import views
from django.urls import path
from .views import UserRegisterView,  PasswordsChangeView
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
   path('register/', UserRegisterView.as_view(), name="register"),
   path('password/', PasswordsChangeView.as_view(template_name='registration/change-password.html')),
   path('password_success/', views.Password_Success, name="password_success"),
]