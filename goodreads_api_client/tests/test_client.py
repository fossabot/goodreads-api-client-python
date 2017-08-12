import unittest

from goodreads_api_client.client import Client


class TestClient(unittest.TestCase):
    def test_init_default(self):
        client = Client(developer_key='fuubar', base_url='http://example.com')

        self.assertEqual(client.developer_key, 'fuubar')
        self.assertEqual(client.base_url, 'http://example.com')

    def test_init_override(self):
        client = Client(developer_key='barbaz')

        self.assertEqual(client.developer_key, 'barbaz')
        self.assertEqual(client.base_url, 'https://goodreads.com')