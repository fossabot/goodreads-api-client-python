import os


developer_key = os.environ.get('GOODREADS_API_KEY', 'fuubar')

__all__ = [
    'developer_key',
]
