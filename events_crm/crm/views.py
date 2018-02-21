from django.http import HttpResponse
from django.template import loader

from .models import Event

def index(request):
    events = Event.objects.all().values('id','name', 'start_date', 'end_date')
    template = loader.get_template('calendar.html')
    return HttpResponse(template.render({'events' : events}, request))
