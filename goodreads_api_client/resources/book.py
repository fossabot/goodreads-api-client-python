# -*- coding: utf-8 -*-
"""Module containing book resource class."""

from typing import Iterable
from goodreads_api_client.resources.base import Resource


class Book(Resource):
    def isbn_to_id(self, isbns: Iterable[str]):
        pass

    def show(self, id_: str):
        endpoint = f'book/show/{id_}.xml'
        res = self._transport.req(endpoint=endpoint)
        return res['book']

