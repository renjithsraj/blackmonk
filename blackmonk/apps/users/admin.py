from django.contrib import admin
from apps.users.models import User
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'first_name', 'last_name', 'email', 'dob', 
        'is_staff', 'is_superuser', 'is_active', 'date_joined', 'last_login']
    list_filter = ['is_staff', 'is_superuser']
    search_fields = ('username', 'firstname', 'lastname', 'email')
