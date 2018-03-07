# Generated by Django 2.0.2 on 2018-03-07 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0008_auto_20180227_2257'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('notes_text_field', models.TextField()),
                ('daily_price', models.PositiveIntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='services',
            field=models.ManyToManyField(blank=True, to='crm.Service'),
        ),
    ]