from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField
from django.utils.translation import gettext as _
from django.contrib.contenttypes.models import ContentType

# BaseModel
class BaseModel(models.Model):
    """ This is will not create an table in database """
    created = models.DateTimeField(_('Created'), auto_now_add=True)
    updated = models.DateTimeField(_('Updated'), auto_now=True)
    is_active = models.BooleanField(_('Active'), default=True)

    class Meta:
        abstract = True

# User
class UserPermission(BaseModel):
    role = models.CharField(_('Role'), max_length=255, null=True, blank=True)
    permissions = models.CharField(_('Permissions'), null=True, blank=True, max_length=255)
    model = models.ForeignKey(ContentType, related_name='permissions', on_delete=models.CASCADE)
    permission_code = models.CharField(_('Code'), max_length=255, null=True, blank=True)
    permission_name = models.CharField(_('Name'), max_length=255, null=True, blank=True)
    group = models.CharField(_('Group'), max_length=255, null=True, blank=True)

    def __str__(self):
        return self.permission_name


# User
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


class Project(BaseModel):
    class PROJECT_TYPES(models.TextChoices):
        ECOMMERCE = 'EC', _('Ecommerce')
        ANALYTICS = 'AL', _('Analytics')
        BLOG = 'BL', _('Blog')
        IMAGE = 'IM', _('Image Gallery')
        PERSONAL = 'PR', _('Personal')

    user = models.ForeignKey(User, related_name='projects', on_delete=models.CASCADE)
    project_name = models.CharField(_('Project Name'), max_length=255)
    project_type = models.CharField(_('Project Type'), max_length=2, 
        choices=PROJECT_TYPES.choices, null=True, blank=True)
    project_desc = models.TextField(_('Project Description'), null=True, blank=True)
    is_expired = models.BooleanField(_('Expired'), null=True, blank=True)
    download_count = models.IntegerField(_('Download Count'), null=True, blank=True)
    class Meta:
        verbose_name = _("Project")
        verbose_name_plural = _("Projects")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Project_detail", kwargs={"pk": self.pk})
