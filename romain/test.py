import unittest
from main import convert_int_to_roman


class TestConvertToInt(unittest.TestCase):
    def test_convert_to_five(self):
        self.assertEqual(convert_int_to_roman(5), "V")
        
    def test_convert_to_nine(self):
        self.assertEqual(convert_int_to_roman(9), "IX")
        
    def test_convert_to_forty(self):
        self.assertEqual(convert_int_to_roman(40), "XL")
        
    def test_convert_to_nieteen_eighty_four(self):
        self.assertEqual(convert_int_to_roman(1984), "MCMIV")    