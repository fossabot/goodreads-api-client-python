# -*- coding: utf-8 -*-
"""Module containing series resource class."""

from goodreads_api_client.resources.base import Resource


class Series(Resource):
    def list(self, author_id: str):
        endpoint = 'series/list'
        params = {
            'id': author_id,
        }
        res = self._transport.req(endpoint=endpoint, params=params)
        return res['series_works']['series_work']

    def show(self, id_: str):
        endpoint = f'series/show/{id_}.xml'
        res = self._transport.req(endpoint=endpoint)
        return res['series']

    def work(self, work_id: str):
        endpoint = f'series/work/{work_id}'
        res = self._transport.req(endpoint=endpoint)
        return res['series_works']['series_work']
