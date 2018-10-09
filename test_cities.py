import unittest
from city_functions import city_format

class CitiesTestCase(unittest.TestCase):
    def test_city_country(self):
        func_output = city_format('tampa', 'america')
        self.assertEqual(func_output, 'Tampa, America')

    def test_city_country_population(self):
        func_output = city_format('tampa', 'united states', '500000')
        self.assertEqual(func_output, 'Tampa, United States - 500000')

unittest.main()
