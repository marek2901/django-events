# Generated by Django 2.0.2 on 2018-02-25 17:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('crm', '0002_auto_20180221_2229'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
