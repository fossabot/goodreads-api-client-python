# -*- coding: utf-8 -*-
"""Module containing auth resource class."""

from goodreads_api_client.exceptions import OauthEndpointNotImplemented
from goodreads_api_client.resources.base import Resource


class Auth(Resource):
    def user(self):
        raise OauthEndpointNotImplemented('auth.user')
