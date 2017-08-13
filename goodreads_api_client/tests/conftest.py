import os

from vcr import VCR


developer_key = os.environ.get('GOODREADS_API_KEY', 'fuubar')


def make_vcr():
    cassette_library_dir = os.path.join(os.path.dirname(__file__),
                                        'fixtures',
                                        'cassettes')
    return VCR(cassette_library_dir=cassette_library_dir,
               filter_query_parameters=['key'],
               record_mode='new_episodes')


vcr = make_vcr()

__all__ = [
    'developer_key',
    'vcr',
]
