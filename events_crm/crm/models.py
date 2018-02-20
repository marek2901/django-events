from django.db import models
from django.utils import timezone


class Equipement(models.Model):
    name = models.CharField(max_length=200)
    serial_n = models.CharField(max_length=200)
    purchase_date = models.DateTimeField(blank=True, null=True)
    notes_text_field = models.TextField()
    daily_price = models.PositiveIntegerField()


class Event(models.Model):
    # customer = models.ForeignKey('auth.User', on_delete=models.CASCADE) TODO
    name = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateTimeField(
        blank=True, null=True)
    end_date = models.DateTimeField(
        blank=True, null=True)
    created_date = models.DateTimeField(
        default=timezone.now)
    equipements = models.ManyToManyField(Equipement)

    def __str__(self):
        return self.name