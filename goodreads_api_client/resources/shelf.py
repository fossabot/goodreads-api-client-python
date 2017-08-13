# -*- coding: utf-8 -*-
"""Module containing user resource class."""

from goodreads_api_client.resources.base import Resource


class Shelf(Resource):
    def add_to_shelf(self):
        raise NotImplementedError('OAuth not yet supported by this library')

    def add_books_to_shelves(self):
        raise NotImplementedError('OAuth not yet supported by this library')

    def list(self, user_id: str):
        endpoint = 'shelf/list.xml'
        params = {
            'user_id': user_id,
        }
        res = self._transport.req(endpoint=endpoint, params=params)
        return res['shelves']
