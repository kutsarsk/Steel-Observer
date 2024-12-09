from django.contrib import admin

from Steel_Observer.accounts.models import AppUser, Profile


@admin.register(AppUser)
class AppUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_active', 'is_staff', 'is_superuser')
    search_fields = ('email', 'is_active', 'is_staff', 'is_superuser')
    list_filter = ('email', 'is_active', 'is_staff', 'is_superuser')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'role')
    search_fields = ('user', 'first_name', 'last_name', 'role')
    list_filter = ('user', 'first_name', 'last_name', 'role')
