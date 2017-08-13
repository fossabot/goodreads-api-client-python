# -*- coding: utf-8 -*-
"""Module containing author following resource class."""

from goodreads_api_client.resources.base import Resource


class AuthorFollowing(Resource):
    def create(self):
        raise NotImplementedError('OAuth not yet supported by this library')

    def destroy(self):
        raise NotImplementedError('OAuth not yet supported by this library')

    def show(self, id_: str):
        raise NotImplementedError('OAuth not yet supported by this library')
