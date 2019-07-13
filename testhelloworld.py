import unittest
import helloworld 

class TestHello(unittest.TestCase):

    def setUp(self):
        helloworld.app.testing = True
        self.app = helloworld.app.test_client()

    def test_hello(self):
        rv = self.app.get('/')
        self.assertEqual(rv.status, '200 OK')
        self.assertEqual(rv.data, b'Hello World')

if __name__ == '__main__':
    unittest.main()