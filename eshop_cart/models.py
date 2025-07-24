from django.db import models

from eshop.settings import AUTH_USER_MODEL
from eshop_products.models import Products

# Create your models here.


class Cart(models.Model):
    owner = models.ForeignKey(to=AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_paid = models.BooleanField(("is paid"), default=False)
    payment_date = models.DateTimeField(
        verbose_name='payment date', blank=True, null=True)

    class Meta:
        ordering = ('-id',)
        verbose_name = ('Card')
        verbose_name_plural = ('Cards')

    def __str__(self):
        return self.owner.get_full_name()


class CartDetail(models.Model):
    cart = models.ForeignKey(to=Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Products, on_delete=models.CASCADE)
    price = models.IntegerField()
    count = models.IntegerField()

    class Meta:
        ordering = ('-id',)
        verbose_name = ('Cart History')
        verbose_name_plural = ('Carts History')

    def __str__(self) -> str:
        return self.product.__str__()

    def sum_total(self):
        return self.price * self.count
