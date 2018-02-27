from django.test import TestCase


import datetime
import pytz

from crm.models import Event
from crm.policies.event_retrival_policy import event_or_404, events_for_user

from django.contrib.auth.models import User
from django.http import Http404


class EventRetrivalPolicyTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username='testuser',
            password='testpswd!@#R'
        )
        self.other_user = User.objects.create(
            username='testuserother',
            password='testpswd!@#R'
        )
        self.moderator = User.objects.create(
            username='moderatoro',
            password='testpswd!@#R'
        )
        self.super_user = User.objects.create_superuser(
            'foo', password='testpswd!@#R', email='tert@admin.com'
        )
        self.event = Event.objects.create(
            name='Test Event',
            description='Test Event desc',
            start_date=datetime.datetime(2011, 8, 15, 8, 15, 12, 0, pytz.UTC),
            end_date=datetime.datetime(2011, 8, 25, 8, 15, 12, 0, pytz.UTC),
        )
        self.event.users.add(self.user)
        self.event.moderators.add(self.moderator)

        self.other_event = Event.objects.create(
            name='OTHER Test Event',
            description='Test Event desc',
            start_date=datetime.datetime(2011, 8, 15, 8, 15, 12, 0, pytz.UTC),
            end_date=datetime.datetime(2011, 8, 25, 8, 15, 12, 0, pytz.UTC),
        )

    def test_event_retrived_when_user_can_see(self):
        self.assertEqual(
            self.event,
            event_or_404(self.user, self.event.id)
        )

    def test_event_retrived_when_user_can_see_and_moderate(self):
        self.event.moderators.add(self.user)
        self.assertEqual(
            self.event,
            event_or_404(self.user, self.event.id)
        )

    def test_event_retrived_when_user_id_moderator(self):
        self.assertEqual(
            self.event,
            event_or_404(self.moderator, self.event.id)
        )

    def test_404_when_user_cannot_retreive(self):
        with self.assertRaises(Http404):
            event_or_404(self.other_user, self.event.id)

    def test_event_retreived_when_user_is_admin(self):
        self.assertEqual(
            self.event,
            event_or_404(self.super_user, self.event.id)
        )

    def test_evets_for_user_returns_owned_event(self):
        self.assertEqual(
            [self.event],
            list(events_for_user(self.user).all())
        )

    def test_evets_for_user_returns_owned_or_moderated_event(self):
        self.event.moderators.add(self.user)
        self.assertEqual(
            [self.event],
            list(events_for_user(self.user).all())
        )

    def test_evets_for_user_returns_moderated_event(self):
        self.assertEqual(
            [self.event],
            list(events_for_user(self.moderator).all())
        )

    def test_all_events_for_admin(self):
        self.assertEqual(
            [self.event, self.other_event],
            list(events_for_user(self.super_user).all())
        )
