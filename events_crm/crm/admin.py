from django.contrib import admin
from crm.models import Event, Equipement, Service, Profile, Skill

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

admin.site.register(Event)
admin.site.register(Equipement)
admin.site.register(Service)


#  Extended user model for Django admin

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'


class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )
    list_display = ('username', 'email', 'skills', 'hourly_rate')

    def skills(self, instance):
        return ', '.join(
            instance.profile.skills.all().values_list('name', flat=True)
        )

    def hourly_rate(self, instance):
        return instance.profile.hourly_rate

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Skill)
