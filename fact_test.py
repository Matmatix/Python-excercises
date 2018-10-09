import unittest
from factorial import fact
class FactTestCase(unittest.TestCase):
    def test_fac(self):
        func_output = fact(7)
        self.assertEqual(func_output, 5040)

    def test_fac_special(self):
        func_output = fact(0)
        self.assertEqual(func_output, 1)

    def test_fac_negative(self):
        func_output = fact(-8)
        self.assertEqual(func_output, -40320)

    def test_fac_neg_zero(self):
        func_output = fact(-0)
        self.assertEqual(func_output, 1)
unittest.main()
