# -*- coding: utf-8 -*-
"""Module containing user status resource class."""

from goodreads_api_client.resources.base import Resource


class UserStatus(Resource):
    def create(self):
        raise NotImplementedError('OAuth not yet supported by this library')

    def destroy(self):
        raise NotImplementedError('OAuth not yet supported by this library')

    def index(self):
        raise NotImplementedError('OAuth not yet supported by this library')

    def show(self, id_: str):
        endpoint = f'user_status/show/{id_}'
        res = self._transport.req(endpoint=endpoint)
        return res['user_status']
