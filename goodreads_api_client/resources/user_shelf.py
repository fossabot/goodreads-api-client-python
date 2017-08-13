# -*- coding: utf-8 -*-
"""Module containing user shelf resource class."""

from goodreads_api_client.resources.base import Resource


class UserShelf(Resource):
    def create(self):
        raise NotImplementedError('OAuth not yet supported by this library')

    def update(self):
        raise NotImplementedError('OAuth not yet supported by this library')
