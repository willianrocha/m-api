from django.test import SimpleTestCase, Client, TestCase
import mock
from .external import Marvel
from . import views
# Create your tests here.


class ViewsTestCase(TestCase):
    def setUp(self):
        self.name = 'Spider-Man (Ultimate)'
        self.char_id = '1011010'
        self.comic_id = '38400'
        self.client = Client()

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_search(self):
        views.search = mock.Mock()
        template = mock.Mock()
        context = {}
        views.search.return_value = [context, template]
        response = self.client.post('/', {'char_name': self.name})
        views.search.assert_called_once()
        self.assertEqual(response.status_code, 200)

    # TODO Bad tests, have to mock Marvel() call inside the views functions
    def test_character(self):
        response = self.client.get('/character/%s/' % self.char_id)
        self.assertEqual(response.status_code, 200)

    def test_comic(self):
        response = self.client.get('/comic/%s/' % self.comic_id)
        self.assertEqual(response.status_code, 200)

# class MarvelTestCase(SimpleTestCase):
#     def setUp(self):
#         self.marvel = Marvel()
#         self.name = 'Spider-Man (Ultimate)'
#         self.char_id = '1011010'
#         self.comic_id = '38400'
#
#     def test_invalid_hash(self):
#         '''
#         https://developer.marvel.com/documentation/authorization
#         '''
#         self.marvel.private_key = ''
#         response = self.marvel.get_characteres(self.name)
#
#         self.assertEqual(response.status_code, 401)
