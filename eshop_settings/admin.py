from django.contrib import admin

from .models import Settings


class SettingsAdmin(admin.ModelAdmin):
    list_display = ['title']


admin.site.register(Settings, SettingsAdmin)
