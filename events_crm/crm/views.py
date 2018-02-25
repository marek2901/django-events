from django.shortcuts import render

from django.contrib.auth.decorators import login_required

from crm.policies.event_retrival_policy import event_or_404, events_for_user

from .models import Event


@login_required
def index(request):
    events = events_for_user(request.user)\
        .values('id', 'name', 'start_date', 'end_date')

    return render(request, 'calendar.html', {
        'events': events,
    })


@login_required
def single_event(request, eid):
    event = event_or_404(request.user, eid)
    return render(request, 'event.html', {
        'event': event,
    })
