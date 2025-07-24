from django.db import models

# Create your models here.


class ProductsCategories(models.Model):
    title = models.CharField(max_length=150)
    name = models.CharField(max_length=150)
    is_active = models.BooleanField(
        ('active'),
        default=True,
        help_text=(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )

    class Meta:
        ordering = ('-id',)
        verbose_name = ('ProductsCategory')
        verbose_name_plural = ('ProductsCategories')

    def __str__(self):
        return self.title
