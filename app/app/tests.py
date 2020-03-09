from django.test import TestCase
from app.calc import add, substract


class CalcTests(TestCase):

    def test_add_numbers(self):
        """Test adding two numbers"""
        self.assertEqual(add(3, 8), 11)

    def test_substract_numbers(self):
        self.assertEqual(substract(8, 3), 5)
