from django.urls import path
from apps.users.views import home, RegisterView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name='home'),
    path('accounts/login', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/register', RegisterView.as_view(), name='register'),
]