from django.urls import path
from apps.users.views import home

urlpatterns = [
    path('', home, name='home')
]