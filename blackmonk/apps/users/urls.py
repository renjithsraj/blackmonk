from django.urls import path
from apps.users.views import home
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name='home'),
    path('login', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
]