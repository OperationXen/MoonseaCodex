from copy import copy
from unittest import mock

from rest_framework.status import *
from django.test import TestCase
from django.urls import reverse

from codex.models import CodexUser


class TestCodexUserPasswordReset(TestCase):
    """ User account self recovery testing """
    fixtures = ['test_users']

    valid_data = {
        'email': 'testuser1@moonseacodex.local',
    }

    @mock.patch('codex.models.users.CodexUser.email_user')
    def test_trigger_password_reset_email(self, mock_email_user) -> None:
        """ A user can request a password reset email """
        test_data = copy(self.valid_data)
        
        response = self.client.post(reverse('forgot_password'), test_data)
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(mock_email_user.called, True)
        (subject, contents) = mock_email_user.call_args[0]
        self.assertIn("Moonsea Codex password reset", subject)

    @mock.patch('codex.models.users.CodexUser.email_user')
    def test_cannot_enumerate_user_emails(self, mock_email_user) -> None:
        """ Requesting invalid password resets does not allow an attacker to deduce which accounts are valid """
        test_data = copy(self.valid_data)

        response = self.client.post(reverse('forgot_password'), test_data)
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(mock_email_user.call_count, 1)
        
        test_data['email'] = "DoesNotExist@moonseacodex.local"
        response = self.client.post(reverse('forgot_password'), test_data)
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(mock_email_user.call_count, 1)

    @mock.patch('codex.utils.email.send_password_reset_email')
    def test_token_allows_password_reset(self, mock_send_password_reset_email) -> None:
        """ Check that the forgot password gives us a token that will allow a password reset """
        forgot_data = copy(self.valid_data)
        user = CodexUser.objects.get(email = forgot_data['email'])
        new_password = 'updatedtestpassword'
        self.assertFalse(user.check_password(new_password))

        forgot_response = self.client.post(reverse('forgot_password'), forgot_data)
        self.assertEqual(forgot_response.status_code, HTTP_200_OK)
        (_, user, activation_token) = mock_send_password_reset_email.call_args[0]     
        
        reset_data = {'user_id': user.pk, 'token': activation_token, 'password': new_password}
        reset_response = self.client.post(reverse('password_reset'), reset_data)
        self.assertEqual(reset_response.status_code, HTTP_200_OK)
        user.refresh_from_db()
        self.assertTrue(user.check_password(new_password))

    def test_token_cannot_be_reused(self):
        pass