import unittest
import taskone



class TestSuma(unittest.TestCase):
    def test_skaiciu_suma(self):
        self.assertEqual(9, taskone.skaiciu_suma(9, 3, 4))
        # self.assertNotEqual(taskone.skaiciu_suma(1, 1, 1), 0)

