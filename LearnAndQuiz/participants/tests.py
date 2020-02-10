from django.contrib.auth.models import User
from django.test import TestCase


class LogInTest(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'something',
            'password': 'something'}
        User.objects.create_user(**self.credentials)

    def test_login(self):
        # send login data
        response = self.client.post('/signin/', self.credentials, follow=True)
        # should be logged in now
        self.assertTrue(response.context['user'].is_active)