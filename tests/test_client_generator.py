import unittest
import britney
import britney_utils
from six import u
from britney.middleware import format, auth


class TestClientGenerator(unittest.TestCase):
    """
    """

    def setUp(self):
        self.description = 'https://raw.github.com/agrausem/britney/master/tests/descriptions/api.json'

    def test_basic_client(self):
        client = britney_utils.get_client('test', self.description, reset=True)
        self.assertEqual(client.base_url, u('http://test.api.org/'))
        self.assertIsInstance(client.test, britney.core.SporeMethod)

    def test_changing_base_url(self):
        client = britney_utils.get_client('test2', 
                                          self.description, 
                                          base_url='http://test.api.org/v2/',
                                          reset=True)
        self.assertEqual(client.base_url, u('http://test.api.org/v2/'))

    def test_caching_client(self):
        client = britney_utils.get_client('test', self.description, reset=True)
        client2 = britney_utils.get_client('test', self.description)
        self.assertEqual(client, client2)

        client2 = britney_utils.get_client('test2', self.description)
        self.assertNotEqual(client, client2)

        client3 = britney_utils.get_client('test', self.description, 
                                           reset=True)
        self.assertNotEqual(client, client3)


    def test_adding_middlewares(self):
        middlewares = (
            (format.Json, {'predicate': lambda: True}),
            (auth.Basic, {'username': 'toto', 'password': 'xxxxxx'})
        )
        client = britney_utils.get_client('test', self.description, reset=True,
                                          middlewares=middlewares)
        self.assertEqual(len(client.middlewares), 2)
        self.assertIsInstance(client.middlewares[0][1], format.Json)
        self.assertIsInstance(client.middlewares[1][1], auth.Basic)
