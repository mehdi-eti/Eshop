# Generated by Django 3.2.3 on 2021-05-29 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(default=False, help_text='Designates whether the user can log into this             admin site. and have permission to create staff user.', verbose_name='admin'),
        ),
    ]
