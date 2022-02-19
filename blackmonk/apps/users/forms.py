from apps.users.models import User
from django import forms
from django.core.exceptions import ValidationError

class UserForm(forms.ModelForm):
    username = forms.CharField(label='Username', max_length=255, min_length=6)
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        if not username:
            raise ValidationError('Username must be a valid')
        user = User.objects.get(username=username)
        if user.count() > 0:
            raise ValidationError('Username already exists')
        return username

    def clean_mail(self):
        email = self.cleaned_data['email'].lower()
        if not email:
            raise ValidationError('Email is not valid')
        user = User.objects.get(email=email)
        if user.count() > 0:
            raise ValidationError('Email already exists')
        return email
    
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")
        raise password2
    
    def save(self, commit=True):
        user = User.objects.get_or_create(
            username = self.cleaned_data.get('username'),
            email = self.cleaned_data.get('email')
        )
        return user


