from django.contrib import admin

from .models import Tags

# Register your models here.


class TagsAdmin(admin.ModelAdmin):
    list_display = ['tittle', 'slug', 'is_active']

    class Meta:
        model = Tags


admin.site.register(Tags, TagsAdmin)
