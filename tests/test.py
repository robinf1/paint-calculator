import paint_calculator
import unittest
from fractions import Fraction

class MyTestCase(unittest.TestCase):

    def setUp(self):
        paint_calculator.app.testing = True
        self.app = paint_calculator.app.test_client()


    def test_home(self):
        result = self.app.get('/')
        data = [Fraction(1,4),Fraction(1,4),Fraction(2,5)]
        result = sum(data)
        self.assertEqual(result, 1)