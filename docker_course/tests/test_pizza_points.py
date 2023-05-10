import unittest
from pizza_points import PizzaPoints


class TestEligibleCustomers(unittest.TestCase):
    
    eligible_customers = PizzaPoints.check_for_eligible()
    
    def test_no_eligible_customers(self):    
        customers = {
            'Kazys': [5, 7, 9],
            'Petras': [10, 12],
            'Jonas': [2, 3, 4, 5]
        }
        self.assertEqual(PizzaPoints.check_for_eligible((customers, 5, 100), []))
    
    def test_some_eligible_customers(self):
        customers = {
            'Kazys': [10, 12, 15, 18],
            'Petras': [20, 25, 30],
            'Jonas': [1, 7, 9, 2, 13]
        }
        self.assertEqual(PizzaPoints.check_for_eligible((customers, 3, 10), ['Kazys', 'Petras']))
    
    def test_all_eligible_customers(self):
        customers = {
            'Kazys': [10, 12, 15, 18],
            'Petras': [20, 25, 30],
            'Jonas': [5, 7, 9, 11, 13]
        }
        self.assertEqual(PizzaPoints.check_for_eligible(customers, 2, 5), ['Kazys', 'Petras', 'Jonas'])