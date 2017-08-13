# -*- coding: utf-8 -*-
"""
goodreads_api_client.resources
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Holds classes for each Goodreads API Resource a user can interact with via
the Goodreads API
"""

from goodreads_api_client.resources.author import Author
from goodreads_api_client.resources.book import Book
from goodreads_api_client.resources.topic import Topic
from goodreads_api_client.resources.user import User
from goodreads_api_client.resources.user_status import UserStatus

__all__ = ['Author', 'Book', 'Topic', 'User', 'UserStatus']
