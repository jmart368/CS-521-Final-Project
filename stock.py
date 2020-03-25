"""
Name: Jose Martinez
Final Project
Description: Set a stock class for the list of stocks
"""

import unittest


class Stock():
    """
    Construct a stock object
    """

    def __init__(self, name, tickler, price):
        self.__name = name
        self.__tickler = tickler
        self.__price = price

    def __str__(self):
        return 'name ' + str(self.name)
        'tickler ' + str(self.tickler)
        'price ' + str(self.price)

    def get_name(self):
        """retrieves the name of stock"""
        return self.__name

    def set_name(self, name):
        """sets the name of stock"""
        self.__name = name

    def get_tickler(self):
        """retrieves the name of the tickler"""
        return self.__tickler

    def set_tickler(self, tickler):
        """sets the name of the tickler"""
        self.__tickler = tickler

    def get_price(self):
        """retrieves the price"""
        return self.__price

    def set_price(self, price):
        """sets the price"""
        self.__price = price


class test_strings(unittest.TestCase):
    """
    Unit test for the capilzation of strings
    """

    def test_upper(self):
        """ensures that the headers will be upper case"""
        self.assertEqual('name'.upper(), 'NAME')
        self.assertEqual('tickler'.upper(), 'TICKLER')
        self.assertEqual('price'.upper(), 'PRICE')

    def test_isupper(self):
        """test the headers for upper case"""
        self.assertTrue('NAME'.isupper())
        self.assertFalse('Name'.isupper())
        self.assertTrue('TICKLER'.isupper())
        self.assertFalse('Tickler'.isupper())
        self.assertTrue('PRICE'.isupper())
        self.assertFalse('Price'.isupper())


if __name__ == '__main__':
    unittest.main()
