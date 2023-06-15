import unittest
from main import FizzBuzz


class TestConvertToInt(unittest.TestCase):
     def test_division_by_three(self):
        fizz_buzz = FizzBuzz(3)
        result = fizz_buzz.division_by_three()
        self.assertEqual(result,"fizz", "fizz" )
       
     def test_division_by_five(self):
        fizz_buzz = FizzBuzz(5)
        result = fizz_buzz.division_by_five()
        self.assertEqual(result,"buzz", "buzz" )
    
     def test_division_by_three_and_five(self):
        fizz_buzz = FizzBuzz(15)
        result = fizz_buzz.division_by_three_and_five()
        self.assertEqual(result,"fizzbuzz", "fizzbuzz" )