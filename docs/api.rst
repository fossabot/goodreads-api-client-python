.. _api:

API Documentation
=================

.. automodule:: goodreads_api_client

This part of the documentation covers the interfaces of goodreads_api_client. 

Main Interface
--------------

You'll primarily use goodreads_api_client via the :class:`Client <Client>` it provides.

.. autoclass:: Client
    :members:

All other endpoints are provided through resource attributes on the :class:`Client <Client>`

.. _api-resources:

Resources
---------

.. autoclass:: goodreads_api_client.resources.author.Author
    :members:
    :show-inheritance:
.. autoclass:: goodreads_api_client.resources.book.Book
    :members:
    :show-inheritance:
.. autoclass:: goodreads_api_client.resources.comment.Comment
    :members:
    :show-inheritance:
.. autoclass:: goodreads_api_client.resources.event.Event
    :members:
    :show-inheritance:
.. autoclass:: goodreads_api_client.resources.group.Group
    :members:
    :show-inheritance:
.. autoclass:: goodreads_api_client.resources.read_status.ReadStatus
    :members:
    :show-inheritance:
.. autoclass:: goodreads_api_client.resources.recommendation.Recommendation
    :members:
    :show-inheritance:
.. autoclass:: goodreads_api_client.resources.review.Review
    :members:
    :show-inheritance:
.. autoclass:: goodreads_api_client.resources.series.Series
    :members:
    :show-inheritance:
.. autoclass:: goodreads_api_client.resources.shelf.Shelf
    :members:
    :show-inheritance:
.. autoclass:: goodreads_api_client.resources.topic.Topic
    :members:
    :show-inheritance:
.. autoclass:: goodreads_api_client.resources.user.User
    :members:
    :show-inheritance:
.. autoclass:: goodreads_api_client.resources.user_status.UserStatus
    :members:
    :show-inheritance:

Lower-Level Classes
-------------------

.. autoclass:: goodreads_api_client.transport.Transport
    :members:
    :show-inheritance:

Exceptions
----------

.. autoexception:: goodreads_api_client.exceptions.GoodreadsApiClientException
    :show-inheritance:
.. autoexception:: goodreads_api_client.exceptions.OauthEndpointNotImplemented
    :show-inheritance:
.. autoexception:: goodreads_api_client.exceptions.ExtraApiPermissionsRequired
    :show-inheritance:
