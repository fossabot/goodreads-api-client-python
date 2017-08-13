# -*- coding: utf-8 -*-
"""Module containing transport that underlies all requests made to the Goodreads API"""

import requests
import xmltodict


class Transport(object):
    """Makes requests to Goodreads API and applies lightweight transform to response."""

    def __init__(self, developer_key: str, base_url: str=None):
        """Initialize with credentials.

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

    def _req(self, method: str='GET', endpoint: str=None, params: dict=None, data: dict=None):
        if params is None:
            params = {}

        res = requests.request(
            method=method,
            url=f'{self.base_url}/{endpoint}',
            params={
                'key': self.developer_key,
                **params
            },
            data=data
        )

        res.raise_for_status()
        return res

    @staticmethod
    def _transform_res(res):
        content = xmltodict.parse(res.text)
        return content['GoodreadsResponse']

    def req(self, method: str='GET', endpoint: str=None, params: dict=None, data: dict=None):
        res = self._req(method, endpoint, params, data)
        return Transport._transform_res(res)
