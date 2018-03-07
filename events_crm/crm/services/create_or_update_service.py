from crm.models import Service


def call(form, service=None):
    if not service:
        return Service.objects.create(
            name=form['name'].value(),
            notes_text_field=form['notes_text_field'].value(),
            daily_price=0
        )
    else:
        service.name = form['name'].value()
        service.notes_text_field = form['notes_text_field'].value()
        service.save()
        return service
