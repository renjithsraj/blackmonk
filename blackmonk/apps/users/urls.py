from django.urls import path
from apps.users.views import home, RegisterView, ActivateAccount
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name='home'),
    path('accounts/login', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/register', RegisterView.as_view(), name='registration'),
    path('activate/<uidb64>/<token>/', ActivateAccount.as_view(), name='activate'),
    path('project/', ActivateAccount.as_view(), name='activate'),
]