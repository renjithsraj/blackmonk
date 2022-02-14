from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField
from django.utils.translation import gettext as _
from django.contrib.contenttypes.models import ContentType

class BaseModel(models.Model):
    """ This is will not create an table in database """
    created = models.DateTimeField(_('Created'), auto_now_add=True)
    updated = models.DateTimeField(_('Updated'), auto_now=True)
    is_active = models.BooleanField(_('Active'), default=True)

    class Meta:
        abstract = True


class UserPermission(BaseModel):
    role = models.CharField(_('Role'), max_length=255, null=True, blank=True)
    permissions = models.CharField(_('Permissions'), null=True, blank=True, max_length=255)
    model = models.ForeignKey(ContentType, related_name='permissions', on_delete=models.CASCADE)
    permission_code = models.CharField(_('Code'), max_length=255, null=True, blank=True)
    permission_name = models.CharField(_('Name'), max_length=255, null=True, blank=True)
    group = models.CharField(_('Group'), max_length=255, null=True, blank=True)

    def __str__(self):
        return self.permission_name





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