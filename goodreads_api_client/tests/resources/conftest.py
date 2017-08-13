import os
import unittest

from vcr import VCR
from goodreads_api_client.tests.conftest import developer_key
from goodreads_api_client.transport import Transport


class ResourceTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Run both child class setup, as well as this class setup.

        Taken from https://gist.github.com/twolfson/13f5f5784f67fd49b245.
        """
        if cls is not ResourceTestCase and cls.setUp is not ResourceTestCase.setUp:
            child_setup = cls.setUp

            def merged_setup(self, *args, **kwargs):
                ResourceTestCase.setUp(self)
                return child_setup(self, *args, **kwargs)

            cls.setUp = merged_setup

    def setUp(self):
        self._transport = Transport(developer_key=developer_key)


def make_vcr():
    cassette_library_dir = os.path.join(os.path.dirname(__file__),
                                        os.pardir,
                                        'fixtures',
                                        'cassettes')
    return VCR(cassette_library_dir=cassette_library_dir,
               filter_query_parameters=['key'],
               record_mode='new_episodes')


vcr = make_vcr()