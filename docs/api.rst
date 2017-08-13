.. _api:

API Documentation
=================

.. module:: goodreads_api_client

This part of the documentation covers the interfaces of goodreads_api_client. 

Main Interface
--------------

You'll primarily use goodreads_api_client via the :class:`Client <Client>` it provides.

.. autoclass:: Client
   :inherited-members:

All other endpoints are provided through resource attributes on the :class:`Client <Client>`

.. _api-resources:

Resources
---------

.. autoclass:: goodreads_api_client.resources.Author
    :inherited-members:
.. autoclass:: goodreads_api_client.resources.Book
    :inherited-members:
.. autoclass:: goodreads_api_client.resources.Comment
    :inherited-members:
.. autoclass:: goodreads_api_client.resources.Event
    :inherited-members:
.. autoclass:: goodreads_api_client.resources.Group
    :inherited-members:
.. autoclass:: goodreads_api_client.resources.ReadStatus
    :inherited-members:
.. autoclass:: goodreads_api_client.resources.Recommendation
    :inherited-members:
.. autoclass:: goodreads_api_client.resources.Review
    :inherited-members:
.. autoclass:: goodreads_api_client.resources.Series
    :inherited-members:
.. autoclass:: goodreads_api_client.resources.Shelf
    :inherited-members:
.. autoclass:: goodreads_api_client.resources.Topic
    :inherited-members:
.. autoclass:: goodreads_api_client.resources.User
    :inherited-members:
.. autoclass:: goodreads_api_client.resources.UserStatus
    :inherited-members:

Lower-Level Classes
-------------------

.. autoclass:: goodreads_api_client.transport.Transport
   :inherited-members:

Exceptions
----------

.. autoexception:: goodreads_api_client.exceptions.GoodreadsApiClientException
.. autoexception:: goodreads_api_client.exceptions.OauthEndpointNotImplemented
.. autoexception:: goodreads_api_client.exceptions.ExtraApiPermissionsRequired
