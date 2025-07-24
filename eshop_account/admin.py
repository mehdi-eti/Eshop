from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import User


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ['phone', 'first_name', 'last_name', 'email',
                    'is_active', 'is_staff', 'is_admin', 'is_consumer', 'is_postman']
    list_filter = ['is_active', 'is_staff',
                   'is_admin', 'is_consumer', 'is_postman']
    list_editable = ['is_active', 'is_staff',
                     'is_admin', 'is_consumer', 'is_postman']
    search_fields = ['first_name', 'phone', 'email', 'last_name']
    fieldsets = (
        (None, {'fields': ('phone', 'password',)}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        ('Permissions', {'fields': ('groups',
                                    'user_permissions', 'is_staff',
                                    'is_active', 'is_admin', 'is_consumer', 'is_postman', 'is_superuser',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'phone', 'email', 'password1', 'password2', 'is_staff', 'is_active', 'is_admin', 'is_consumer',
                'is_postman',
                'is_superuser')}
         ),
    )
    filter_horizontal = ('groups', 'user_permissions',)
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(User, CustomUserAdmin)
