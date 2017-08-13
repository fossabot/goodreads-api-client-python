# -*- coding: utf-8 -*-
"""Module containing topic resource class."""

from goodreads_api_client.resources.base import Resource


class Topic(Resource):
    def create(self):
        raise NotImplementedError('OAuth not yet supported by this library')

    def group_folder(self, id_: str):
        endpoint = f'topic/group_folder/{id_}'
        res = self._transport.req(endpoint=endpoint)
        return res['group_folder']

    def show(self, id_: str):
        endpoint = 'topic/show.xml'
        params = {
            'id': id_,
        }
        res = self._transport.req(endpoint=endpoint, params=params)
        return res['topic']

    def unread_group(self):
        raise NotImplementedError('OAuth not yet supported by this library')
