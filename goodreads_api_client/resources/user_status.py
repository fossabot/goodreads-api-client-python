# -*- coding: utf-8 -*-
"""Module containing user status resource class."""

from goodreads_api_client.exceptions import OauthEndpointNotImplemented
from goodreads_api_client.resources.base import Resource


class UserStatus(Resource):
    def create(self):
        raise OauthEndpointNotImplemented('user_status.create')

    def destroy(self):
        raise OauthEndpointNotImplemented('user_status.destroy')

    def index(self):
        raise OauthEndpointNotImplemented('user_status.index')

    def show(self, id_: str):
        endpoint = f'user_status/show/{id_}'
        res = self._transport.req(endpoint=endpoint)
        return res['user_status']
