from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Profile, NationalSociety

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'

class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)

# Register NationalSociety model
admin.site.register(NationalSociety)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
