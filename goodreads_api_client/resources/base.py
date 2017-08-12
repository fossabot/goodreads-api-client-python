# -*- coding: utf-8 -*-
"""Module containing base resource class."""


class Resource(object):
    """Base resource class. All Goodreads API resource classes should inherit this."""

    def __init__(self, transport=None):
        self._transport = transport
