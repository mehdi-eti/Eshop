from django.contrib import admin

from .models import Sliders

class SlidersAdmin(admin.ModelAdmin):
    list_display = ['title', 'link', 'image', 'is_active']

    class Meta:
        model = Sliders

admin.site.register(Sliders, SlidersAdmin)
