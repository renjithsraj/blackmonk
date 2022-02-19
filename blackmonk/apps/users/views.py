from typing import ValuesView
from django.shortcuts import render
from django.views import View
from apps.users.forms import UserForm
from django.shortcuts import redirect
# Create your views here.

def home(request):
    return render(request, 'home.html')

class RegisterView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'registration/registration.html', {})
    
    def post(self, request, *args, **kwargs):
        form = UserForm(request.POST)
        if form.isvalid():
            user = form.save()
            user.set_password(form.cleaned_data['password'])
            user.is_active = False
            user.save()
            return redirect('/login')
        return render(request, 'registration/registration.html', {'form': form})
    