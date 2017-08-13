# -*- coding: utf-8 -*-
"""Module containing author resource class."""

from goodreads_api_client.resources.base import Resource


class Author(Resource):
    def books(self, id_: str):
        """List books for an author.

        TODO: Add pagination support
        """
        endpoint = f'author/list/{id_}'
        res = self._transport.req(endpoint=endpoint)
        return res['author']['books']

    def show(self, id_: str):
        endpoint = f'author/show/{id_}'
        res = self._transport.req(endpoint=endpoint)
        return res['author']
