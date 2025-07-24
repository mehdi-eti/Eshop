from django.db import models
import os

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    file_name = f"{instance.id}-{instance.title}{ext}"
    return f"products/{file_name}"

# Create your models here.
class Sliders(models.Model):
    title = models.CharField(max_length=150)
    link = models.URLField(max_length=100)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True,
                              upload_to=upload_image_path)
    is_active = models.BooleanField(
        ('active'),
        default=True,
        help_text=(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )

    class Meta:
        ordering = ('id',)
        verbose_name = ('slider')
        verbose_name_plural = ('sliders')

    def __str__(self):
        return self.title
