from django.test import TestCase

from crm.models import Service
from crm.forms import ServiceForm
from crm.services import create_or_update_service


class EventRetrivalPolicyTest(TestCase):
    def setUp(self):
        self.serviceForm = ServiceForm(initial={
            'name': 'TEST NAME',
            'notes_text_field': 'Some notes blablabla'
        })

    def test_creation_of_new_service(self):
        created_one = create_or_update_service.call(self.serviceForm)
        self.assertEqual(Service.objects.latest('id'), created_one)
        self.assertEqual(created_one.name, 'TEST NAME')
        self.assertEqual(created_one.notes_text_field, 'Some notes blablabla')

    def test_update_of_new_service(self):
        existing_one = Service.objects.create(
            name='old value',
            notes_text_field='Wohoa',
            daily_price=0
        )

        updated_one = create_or_update_service.call(
            self.serviceForm, existing_one)

        self.assertEqual(updated_one, existing_one)
        self.assertEqual(Service.objects.latest('id'), existing_one)
        self.assertEqual(Service.objects.latest('id'), updated_one)
        self.assertEqual(updated_one.name, 'TEST NAME')
        self.assertEqual(updated_one.notes_text_field, 'Some notes blablabla')
