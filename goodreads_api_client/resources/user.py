# -*- coding: utf-8 -*-
"""Module containing user resource class."""

from goodreads_api_client.exceptions import OauthEndpointNotImplemented
from goodreads_api_client.resources.base import Resource


class User(Resource):
    def compare(self):
        raise OauthEndpointNotImplemented('user.compare')

    def followers(self):
        raise OauthEndpointNotImplemented('user.followers')

    def following(self):
        raise OauthEndpointNotImplemented('user.following')

    def friends(self):
        raise OauthEndpointNotImplemented('user.friends')

    def show(self, id_: str):
        endpoint = f'user/show/{id_}.xml'
        res = self._transport.req(endpoint=endpoint)
        return res['user']
