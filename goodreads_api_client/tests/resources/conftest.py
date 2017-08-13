import unittest

from goodreads_api_client.tests.conftest import developer_key
from goodreads_api_client.transport import Transport


class ResourceTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Run both child class setup, as well as this class setup.

        Taken from https://gist.github.com/twolfson/13f5f5784f67fd49b245.
        """
        if cls is not ResourceTestCase and \
                cls.setUp is not ResourceTestCase.setUp:
            child_setup = cls.setUp

            def merged_setup(self, *args, **kwargs):
                ResourceTestCase.setUp(self)
                return child_setup(self, *args, **kwargs)

            cls.setUp = merged_setup

    def setUp(self):
        self._transport = Transport(developer_key=developer_key)
