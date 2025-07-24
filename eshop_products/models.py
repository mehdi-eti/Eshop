from django.db import models
from django.utils.translation import gettext_lazy as _
import os

from eshop_products_categories.models import ProductsCategories


# Create Function
def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    file_name = f"{instance.id}-{instance.tittle}{ext}"
    return f"products/{file_name}"


def upload_galleries_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    file_name = f"{instance.id}-{instance.title}{ext}"
    return f"products/gallery/{file_name}"


class ProductManager(models.Manager):
    def get_active_products(self):
        return self.get_queryset().filter(is_active=True)

    def get_by_id(self, pk):
        gs = self.get_queryset().filter(pk=pk, is_active=True)
        if gs.count() == 1:
            return gs.first()
        return None

    def get_related_products(self, product, pk=None):
        qy = self.get_queryset().filter(categories__products=product,
                                        is_active=True).exclude(id=pk).distinct()
        return qy

    def search(self, query):
        allQuery = (models.Q(tittle__icontains=query) |
                    models.Q(descriptsion__icontains=query) |
                    models.Q(tags__tittle__icontains=query))
        return self.get_queryset().filter(allQuery, is_active=True).distinct()

    def get_by_category(self, category_name):
        return self.get_queryset().filter(categories__name__iexact=category_name, is_active=True)


# Create your models here.
class Products(models.Model):
    tittle = models.CharField(max_length=150)
    price = models.IntegerField()
    descriptsion = models.TextField()
    image = models.ImageField(null=True, blank=True,
                              upload_to=upload_image_path)
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    categories = models.ManyToManyField(to=ProductsCategories, blank=True)
    count_visit = models.PositiveIntegerField(default=0)

    objects = ProductManager()

    class Meta:
        ordering = ('-id',)
        verbose_name = _('product')
        verbose_name_plural = _('products')

    def __str__(self):
        return self.tittle

    def get_absolute_url(self):
        return f"{self.id}/{self.tittle.replace(' ','-')}"


class ProductsGallery(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(null=True, upload_to=upload_galleries_image_path)
    products = models.ForeignKey(to=Products, on_delete=models.CASCADE)

    class Meta:
        ordering = ('id',)
        verbose_name = _('gallery')
        verbose_name_plural = _('galleries')

    def __str__(self):
        return self.title
