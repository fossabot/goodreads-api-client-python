# -*- coding: utf-8 -*-
"""Module containing update resource class."""

from goodreads_api_client.resources.base import Resource


class Update(Resource):
    def friends(self):
        raise NotImplementedError('OAuth not yet supported by this library')
