from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Equipement(models.Model):
    name = models.CharField(max_length=200)
    serial_n = models.CharField(max_length=200)
    purchase_date = models.DateTimeField(blank=True, null=True)
    notes_text_field = models.TextField()
    daily_price = models.PositiveIntegerField()

    def __str__(self):
        return 'Wyposażenie: {}'.format(self.name)


class Event(models.Model):
    # customer = models.ForeignKey('auth.User', on_delete=models.CASCADE) TODO
    name = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateTimeField(
        blank=False, null=False)
    end_date = models.DateTimeField(
        blank=False, null=False)
    created_date = models.DateTimeField(
        default=timezone.now)
    equipements = models.ManyToManyField(Equipement, blank=True)
    users = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.name
