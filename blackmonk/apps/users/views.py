from typing import ValuesView
from django.shortcuts import render
from django.views import View
from apps.users.forms import UserForm
from apps.users.models import User
from django.shortcuts import redirect

from apps.users.tokens import account_activation_token
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode

from django.contrib.auth import login
from django.utils.encoding import force_str as force_text

# Create your views here.

def home(request):
    return render(request, 'home.html')

class RegisterView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'registration/registration.html', {})
    
    def prepare_for_activate_mail(self, *args, **kwargs):
        try:
            current_site = get_current_site(kwargs.get('request'))
            user = kwargs.get('user')
            subject = "Activate your BlackMonk Account"
            message = render_to_string('emails/account_activation_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user),
                })
            user.email_user(subject, message)
        except Exception as e:
            raise RuntimeError(f"Something went wrong: {str(e)}")
        return True
        

    
    def post(self, request, *args, **kwargs):
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(form.cleaned_data['password'])
            user.is_active = False
            user.save()
            self.prepare_for_activate_mail(request=request, user=user)
            return redirect('/accounts/login')
        return render(request, 'registration/registration.html', {'form': form})

class ActivateAccount(View):
    
    def get(self, request, uidb64, token, *args, **kwargs):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.profile.email_confirmed = True
            user.save()
            login(request, user)
            messages.success(request, ('Your account have been confirmed.'))
            return redirect('home')
        else:
            messages.warning(request, ('The confirmation link was invalid, possibly because it has already been used.'))
            return redirect('home')