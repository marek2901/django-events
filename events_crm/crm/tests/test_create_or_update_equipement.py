from django.test import TestCase

from crm.models import Equipement
from crm.forms import EquipementForm
from crm.services import create_or_update_equipement


class CreateOrUpdateEquipementTest(TestCase):
    def setUp(self):
        self.equipementForm = EquipementForm(initial={
            'name': 'TEST NAME',
            'notes_text_field': 'Some notes blablabla',
            'serial_n': '#123456'
        })

    def test_creation_of_new_service(self):
        created_one = create_or_update_equipement.call(self.equipementForm)
        self.assertEqual(Equipement.objects.latest('id'), created_one)
        self.assertEqual(created_one.name, 'TEST NAME')
        self.assertEqual(created_one.notes_text_field, 'Some notes blablabla')
        self.assertEqual(created_one.serial_n, '#123456')

    def test_update_of_new_service(self):
        existing_one = Equipement.objects.create(
            name='old value',
            notes_text_field='Wohoa',
            serial_n='#####',
            daily_price=0
        )

        updated_one = create_or_update_equipement.call(
            self.equipementForm, existing_one)

        self.assertEqual(updated_one, existing_one)
        self.assertEqual(Equipement.objects.latest('id'), existing_one)
        self.assertEqual(Equipement.objects.latest('id'), updated_one)
        self.assertEqual(updated_one.name, 'TEST NAME')
        self.assertEqual(updated_one.notes_text_field, 'Some notes blablabla')
        self.assertEqual(updated_one.serial_n, '#123456')
