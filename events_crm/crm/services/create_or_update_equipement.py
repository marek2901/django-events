from crm.models import Equipement


def call(form, equipement=None):
    if not equipement:
        return Equipement.objects.create(
            name=form['name'].value(),
            notes_text_field=form['notes_text_field'].value(),
            serial_n=form['serial_n'].value(),
            daily_price=0
        )
    else:
        equipement.name = form['name'].value()
        equipement.notes_text_field = form['notes_text_field'].value()
        equipement.serial_n = form['serial_n'].value()
        equipement.save()
        return equipement
