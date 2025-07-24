from django.db import models

# Create your models here.


class ContactUs(models.Model):
    full_name = models.CharField(max_length=100, verbose_name='Full name')
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=150)
    text = models.TextField(max_length=250)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ('-id',)
        verbose_name = ('conatc-us message')
        verbose_name_plural = ('Contact-us messages')

    def __str__(self) -> str:
        return self.full_name

    def get_full_name(self):
        return self.full_name

    def get_short_name(self):
        """Return the short name for the user."""
        return self.full_name
