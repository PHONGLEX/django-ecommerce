from django.contrib.auth import views as auth_views
from django.urls import path

from .forms import (UserLoginForm)
from . import views


app_name = 'account'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='account/registration/login.html', form_class=UserLoginForm), name='login'),
    path('register/', views.account_register, name='account_register'),
    path('activate/<slug:uidb64>/<slug:token>', views.account_activate, name='activate'),
    path('dashboard/', views.account_dashboard, name='dashboard'),
]