# -*- coding: utf-8 -*-
"""
goodreads_api_client.tests.resources
~~~~~

Contains all goodreads_api_client tests for resource classes.
"""

import os
import unittest

from vcr import VCR
from goodreads_api_client.transport import Transport


GOODREADS_API_KEY = os.environ.get('GOODREADS_API_KEY', 'fuubar')


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
        self._transport = Transport(developer_key=GOODREADS_API_KEY)


def make_vcr():
    cassette_library_dir = os.path.join(os.path.dirname(__file__),
                                        os.pardir,
                                        'fixtures',
                                        'cassettes')
    return VCR(cassette_library_dir=cassette_library_dir,
               filter_query_parameters=['key'],
               record_mode='once')


vcr = make_vcr()
