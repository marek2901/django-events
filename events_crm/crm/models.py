from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from django.dispatch import receiver
from django.db.models.signals import post_save


class Equipement(models.Model):
    name = models.CharField(max_length=200)
    serial_n = models.CharField(max_length=200)
    purchase_date = models.DateTimeField(blank=True, null=True)
    notes_text_field = models.TextField()
    daily_price = models.PositiveIntegerField()

    def __str__(self):
        return 'Wyposażenie: {}'.format(self.name)


class Service(models.Model):
    name = models.CharField(max_length=200)
    notes_text_field = models.TextField()
    daily_price = models.PositiveIntegerField()

    def __str__(self):
        return 'Usługa: {}'.format(self.name)


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
    services = models.ManyToManyField(Service, blank=True)
    users = models.ManyToManyField(User, blank=True, related_name='users')
    moderators = models.ManyToManyField(
        User, blank=True, related_name='moderators')

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return 'Skill: {}'.format(self.name)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    hourly_rate = models.PositiveIntegerField(blank=True, null=True)
    skills = models.ManyToManyField(Skill, blank=True)

    def __str__(self):
        return 'Profil: {}'.format(self.user.username)


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
