from django.http import HttpResponse
from django.template import loader

from django.contrib.auth.decorators import login_required

from .models import Event


@login_required
def index(request):
    events = Event.objects.all().values('id', 'name', 'start_date', 'end_date')
    template = loader.get_template('calendar.html')
    return HttpResponse(template.render({'events': events}, request))
