# -*- coding: utf-8 -*-
"""
goodreads_api_client.resources
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Holds classes for each Goodreads API Resource a user can interact with via
the Goodreads API
"""

from goodreads_api_client.resources.author import Author
from goodreads_api_client.resources.book import Book
from goodreads_api_client.resources.user import User

__all__ = ['Author', 'Book', 'User']
