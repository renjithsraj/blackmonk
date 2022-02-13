from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField
from django.utils.translation import gettext as _



class User(AbstractUser):
    """ Extending Django admin User functional """
    about_me =  RichTextField()
    slug = models.SlugField(max_length= 250, null= True, blank= True, unique= True)
    username = models.CharField(_("Username"), max_length=30, unique=True)
    dob = models.DateField(_("Date of Birth"), null=True, blank=True)
    profile_img = models.ImageField(_("Profile Image"), upload_to='profile', null=True, blank=True)

    phone = models.CharField(_("Phone"), max_length=30, null=True, blank=True)

    class Meta:
        ordering = ('date_joined',)
    
    def __str__(self):
        return self.username

    def age(self):
        pass
    
    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)