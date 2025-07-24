from django.db import models
from django.utils.translation import gettext_lazy as _

from eshop_products.models import Products
from .utils import unique_slug_generator


class Tags(models.Model):
    tittle = models.CharField(max_length=120)
    slug = models.SlugField()
    timestamp = models.TimeField(auto_now_add=True)
    products = models.ManyToManyField(to=Products, blank=True)
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )

    class Meta:
        ordering = ('-id',)
        verbose_name = _('tag')
        verbose_name_plural = _('tags')

    def __str__(self):
        return self.tittle


def tags_presave_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


models.signals.pre_save.connect(tags_presave_receiver, sender=Tags)
