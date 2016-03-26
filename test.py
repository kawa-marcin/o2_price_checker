#!/usr/bin/python
# -*- coding: utf-8 -*-

from o2_price_inspector import (
    O2PriceInspector,
    O2PriceInspectorException
)

from decimal import Decimal
import unittest


class TestO2PriceInspector(unittest.TestCase):
    def setUp(self):
        self.price_inspector = O2PriceInspector()

    def tearDown(self):
        self.price_inspector.close()

    def test_check_price(self):
        price = self.price_inspector.check_price_for('Germany')

        self.assertTrue(type(price), Decimal)

    def test_wrong_country(self):
        with self.assertRaises(O2PriceInspectorException):
            self.price_inspector.check_price_for('NotACountry')

if __name__ == '__main__':
    unittest.main()