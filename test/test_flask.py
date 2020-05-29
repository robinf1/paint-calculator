import unittest
from paint_calculator.run import app


class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_home_page(self):
        """
        Tests if home page is available
        """
        response = self.app.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200, "Response should be 200")
        self.assertIn(b'Enter the number of rooms', response.data, "Should display 'Enter the number of rooms'")

    def test_dimensions_page(self):
        """
        Tests if dimensions page is available when 'rooms' query is present
        """
        response = self.app.get('/dimensions?rooms=3', content_type='html/text')
        self.assertEqual(response.status_code, 200, "Response should be 200")
        self.assertIn(b'length-2', response.data, "Should be three rows of input for query 'rooms=3'")

    def test_results_page(self):
        """
        Tests if results page is available when posted with valid data args
        """
        response = self.app.post(
            '/results',
            data={'length-0':20,'width-0':20,'height-0':20}
            )
        self.assertIn(b'room-1', response.data, "'room-1' should be in table given data args")

    def test_results_page_invalid(self):
        """
        Tests if results page will respond with 405 with incorrect call (GET) method
        """
        response = self.app.get('/results')
        self.assertEqual(response.status_code, 405, "Response should return 405")

    def test_invalid_page(self):
        result = self.app.get('a', content_type='html/text')
        self.assertEqual(result.status_code, 404)