from rest_framework.status import *
from django.test import TestCase
from django.urls import reverse

from codex.models.api_keys import APIKey
from codex.models.users import CodexUser
from codex.models.character import Character


class TestDiscordBotCharacterSearch(TestCase):
    """Tests for DiscordBot API functionality"""
    fixtures = ["test_users", "test_characters", "test_apikeys"]

    def test_apikey_required(self) -> None:
        """ Any query to the discord bot endpoint needs to include an apikey"""
        self.client.logout()
        test_data = {'discord_id': 'Volothamp#0420'}

        response = self.client.post(reverse('discord_lookup', kwargs={'query_type': 'character'}), test_data)
        self.assertEqual(response.status_code, HTTP_403_FORBIDDEN)

    def test_valid_apikey_required(self) -> None:
        """ Any query to the discord bot endpoint needs a valid apikey"""
        self.client.logout()
        test_data = {'apikey': '123123123123123123123123','discord_id': 'Volothamp#0420'}

        response = self.client.post(reverse('discord_lookup', kwargs={'query_type': 'character'}), test_data)
        self.assertEqual(response.status_code, HTTP_403_FORBIDDEN)

    def test_search_by_valid_discord_id(self) -> None:
        """ Check that a discord ID for a player brings back their public characters """
        apikey = APIKey.objects.get(pk=1)
        user = CodexUser.objects.get(username='testuser1')

        test_data = {'apikey': apikey.value, 'discord_id': user.discord_id.lower()}
        response = self.client.post(reverse('discord_lookup', kwargs={'query_type': 'character'}), test_data)
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertIsInstance(response.data, list)
        self.assertGreaterEqual(len(response.data), 2)
        self.assertIn('name', response.data[0])
        self.assertEqual('Meepo', response.data[0]['name'])

    def test_search_by_invalid_discord_id(self) -> None:
        """ Check that a discord ID for a player brings back their public characters """
        apikey = APIKey.objects.get(pk=1)
        user = CodexUser.objects.get(username='testuser1')

        test_data = {'apikey': apikey.value, 'discord_id': 'DrizztGod#0001'}
        response = self.client.post(reverse('discord_lookup', kwargs={'query_type': 'character'}), test_data)
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertIsInstance(response.data, list)
        self.assertGreaterEqual(len(response.data), 0)
