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

    def test_throwexception(self):
        with self.assertRaises(Exception): 
            self.app.get('/throwexception')

if __name__ == '__main__':
    import xmlrunner
    runner = xmlrunner.XMLTestRunner(output='test-reports')
    unittest.main(testRunner=runner)
    unittest.main()