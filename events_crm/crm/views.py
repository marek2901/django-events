from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from crm.policies.event_retrival_policy import event_or_404, events_for_user

from .models import Event, Equipement, Service


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


@login_required
def equipements(request):
    equipement_list = Equipement.objects.all()

    paginator = Paginator(equipement_list, 15)

    page = request.GET.get('page')

    return render(request, 'equipements.html', {
        'equipements': paginator.get_page(page)
    })


@login_required
def equipements(request):
    services_list = Service.objects.all()

    paginator = Paginator(services_list, 15)

    page = request.GET.get('page')

    return render(request, 'services.html', {
        'services': paginator.get_page(page)
    })
