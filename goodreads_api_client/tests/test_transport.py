import unittest

from goodreads_api_client.transport import Transport


class TestTransport(unittest.TestCase):
    def test_init_default(self):
        transport = Transport(developer_key='fuubar',
                              base_url='http://example.com')

        self.assertEqual(transport.developer_key, 'fuubar')
        self.assertEqual(transport.base_url, 'http://example.com')

    def test_init_override(self):
        transport = Transport(developer_key='barbaz')

        self.assertEqual(transport.developer_key, 'barbaz')
        self.assertEqual(transport.base_url, 'https://goodreads.com')
