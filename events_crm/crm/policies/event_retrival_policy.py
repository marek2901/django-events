from crm.models import Event
from django.db.models import Q
from django.http import Http404


def event_or_404(user, event_id):
    event = Event.objects.get(id=event_id)
    if user.is_superuser or\
            (user in event.users.all()) or (user in event.moderators.all()):
        return event
    else:
        raise Http404('Event does not exist')


def events_for_user(user):
    if user.is_superuser:
        return Event.objects
    else:
        return Event.objects\
            .filter(Q(users__in=[user]) | Q(moderators__in=[user])).distinct()
