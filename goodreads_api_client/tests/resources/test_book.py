from goodreads_api_client.resources import Book
from goodreads_api_client.tests.resources import ResourceTestCase, vcr


class TestBook(ResourceTestCase):
    def setUp(self):
        self._book = Book(transport=self._transport)

    @vcr.use_cassette('book/show.yaml')
    def test_show(self):
        book_dict = self._book.show('50')

        self.assertEqual(book_dict['id'], '50')
        self.assertEqual(book_dict['title'], "Hatchet (Brian's Saga, #1)")
