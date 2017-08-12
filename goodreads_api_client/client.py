# -*- coding: utf-8 -*-
"""Module containing client with methods of Goodreads API."""

from goodreads_api_client.resources import *


class Client(object):
    """Makes API Calls to the Goodreads API <https://goodreads.com/api>."""

    def __init__(self, developer_key: str, base_url: str=None):
        """Initialize Goodreads API client with credentials.

        :param str developer_key: Your Goodreads developer key. Find or generate
            one from here <https://goodreads.com/api/keys>
        :param str/None base_url: The base URL to use to contact the Goodreads API.
            Defaults to https://goodreads.com.
        """
        if base_url is None:
            self.base_url = 'https://goodreads.com'
        else:
            self.base_url = base_url

        self.developer_key = developer_key

        self.Book = Book(transport=self._req)

    def _req(self, method, endpoint, params=None, data=None):
        pass

    def book_show(self, id_: str):
        return self.Book.show(id_)

