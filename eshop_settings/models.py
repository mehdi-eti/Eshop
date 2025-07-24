from django.db import models

# Create your models here.
class Settings(models.Model):
    title = models.CharField(max_length=100)
    phone = models.IntegerField()
    fax = models.IntegerField()
    email = models.EmailField(max_length=100)
    about_us = models.TextField(verbose_name='about us')
    copy_right = models.CharField(verbose_name='copy right', max_length=150)
    address = models.TextField(max_length=250, default='')

    class Meta:
        ordering = ('-id',)
        verbose_name = ('setting')
        verbose_name_plural = ('settings')

    def __str__(self) -> str:
        return self.title
