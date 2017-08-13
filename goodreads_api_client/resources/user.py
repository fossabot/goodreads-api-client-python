# -*- coding: utf-8 -*-
"""Module containing user resource class."""

from goodreads_api_client.resources.base import Resource


class User(Resource):
    def show(self, id_: str):
        endpoint = f'user/show/{id_}.xml'
        res = self._transport.req(endpoint=endpoint)
        return res['user']
