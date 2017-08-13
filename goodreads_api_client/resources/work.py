# -*- coding: utf-8 -*-
"""Module containing work resource class."""

from goodreads_api_client.resources.base import Resource


class Work(Resource):
    def editions(self, id_: str):
        raise NotImplementedError('API requires extra permission')
