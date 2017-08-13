# -*- coding: utf-8 -*-
"""Module containing recommendation resource class."""

from goodreads_api_client.exceptions import OauthEndpointNotImplemented
from goodreads_api_client.resources.base import Resource


class Recommendation(Resource):
    def show(self, id_: str):
        raise OauthEndpointNotImplemented('recommendation.show')
