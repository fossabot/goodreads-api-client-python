import unittest

from goodreads_api_client.client import Client
from goodreads_api_client.tests.conftest import developer_key


class TestClient(unittest.TestCase):
    def setUp(self):
        self._client = Client(developer_key=developer_key)

    def test_search_author(self):
        result = self._client.search_author('Murakami')

        self.assertEqual(result['name'], 'Haruki Murakami')

    def test_search_book(self):
        result = self._client.search_book(q='Highprince of War')

        self.assertEqual(int(result['total-results']), 1)
