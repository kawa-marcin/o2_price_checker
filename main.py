#!/usr/bin/python
# -*- coding: utf-8 -*-

from o2_price_inspector import O2PriceInspector


countries = [
    "Canada",
    "Germany",
    "Iceland",
    "Pakistan",
    "Singapore",
    "South Africa"
]

if __name__ == '__main__':
    with O2PriceInspector() as price_inspector:

        for country_name in countries:
            price = price_inspector.check_price_for(country_name)

            print country_name, price
