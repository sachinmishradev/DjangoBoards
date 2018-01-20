from django.core import mail
from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase

class PasswordResetMailTests(TestCase):
    def setUp(self):
        User.objects.create_user(username='sachin', email='sachinmishra199747@gmail.com', password='Hello12345')
        self.response = self.client.post(reverse('password_reset'), { 'email': 'sachinmishra199747@gmail.com' })
        self.email = mail.outbox[0]

    def test_email_subject(self):
        self.assertEqual('[Django Boards] Please reset your password', self.email.subject)

    def test_email_body(self):
        context = self.response.context
        token = context.get('token')
        uid = context.get('uid')
        password_reset_token_url = reverse('password_reset_confirm', kwargs={
            'uidb64': uid,
            'token': token
        })
        self.assertIn(password_reset_token_url, self.email.body)
        self.assertIn('sachin', self.email.body)
        self.assertIn('sachinmishra199747@gmail.com', self.email.body)

    def test_email_to(self):
        self.assertEqual(['sachinmishra199747@gmail.com',], self.email.to)


