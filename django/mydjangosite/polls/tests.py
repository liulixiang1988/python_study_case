"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.utils import timezone
import datetime

from polls.models import Poll


class PollMethodTests(TestCase):
    def test_was_published_recently_with_future_poll(self):
        '''
        was_published_recently should return false with future poll
        '''
        future_poll = Poll(pub_date=timezone.now() + datetime.timedelta(days=10))
        self.assertEqual(future_poll.was_published_recently(), False)

    def test_was_published_recently_with_old_poll(self):
        '''
        was_published_recently should return false with old poll
        '''
        old_poll = Poll(pub_date=timezone.now() - datetime.timedelta(days=10))
        self.assertEqual(old_poll.was_published_recently(), False)

    def test_was_published_recently_with_recent_poll(self):
        '''
        was_published_recently should return true with recent poll
        '''
        recent_poll = Poll(pub_date=timezone.now() - datetime.timedelta(hours=1))
        self.assertEqual(recent_poll.was_published_recently(), True)
