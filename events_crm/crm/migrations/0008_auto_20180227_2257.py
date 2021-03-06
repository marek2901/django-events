# Generated by Django 2.0.2 on 2018-02-27 22:57

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('crm', '0007_auto_20180226_1657'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='moderators',
            field=models.ManyToManyField(blank=True, related_name='moderators', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='event',
            name='users',
            field=models.ManyToManyField(blank=True, related_name='users', to=settings.AUTH_USER_MODEL),
        ),
    ]
