from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator

from crm.policies.event_retrival_policy import event_or_404, events_for_user

from .models import Event, Equipement, Service
from .forms import EquipementForm, ServiceForm
from .services import create_or_update_service


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
def services(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            create_or_update_service.call(form)
            messages.success(request, 'Dodano Usługę')
        else:
            messages.error(request, 'Wystąpiły Błędy')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    else:
        services_list = Service.objects.all()
        paginator = Paginator(services_list, 15)
        page = request.GET.get('page')
        return render(request, 'services.html', {
            'services': paginator.get_page(page),
            'form': ServiceForm(),
        })
