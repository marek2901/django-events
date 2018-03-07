from django import forms


class EquipementForm(forms.Form):
    name = forms.CharField(max_length=200)
    serial_n = forms.CharField(max_length=200)
    notes_text_field = forms.CharField(widget=forms.Textarea)


class ServiceForm(forms.Form):
    name = forms.CharField(max_length=200)
    notes_text_field = forms.CharField(widget=forms.Textarea)
