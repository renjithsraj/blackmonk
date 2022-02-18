from typing import ValuesView
from django.shortcuts import render
from django.views import View
# Create your views here.

def home(request):
    return render(request, 'home.html')

class RegisterView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'registration/registration.html', {})