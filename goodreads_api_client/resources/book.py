# -*- coding: utf-8 -*-
"""Module containing book resource class."""

from goodreads_api_client.resources.base import Resource


class Book(Resource):
    def show(self, id_: str):
        raise NotImplementedError('book.show')
