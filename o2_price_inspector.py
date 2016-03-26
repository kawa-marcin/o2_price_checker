#!/usr/bin/python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from selenium.common.exceptions import NoSuchElementException, TimeoutException

from decimal import Decimal


class O2PriceInspectorException(Exception):
    pass

class O2PriceInspector(object):
    def __init__(self, url=("http://international.o2.co.uk/" 
                            "internationaltariffs/calling_abroad_from_uk")):
        self.url = url

        self.driver = webdriver.Chrome()
        self.driver.get(self.url)
        self.country_input = self.driver.find_element_by_id("countryName")

        self._ajax_load_timeout = 5
        self._ajax_loaded_el = ("//div[@id='paymonthlyTariffPlan']"
                                "//h2[text()[contains(.,'%s')]]")
        self._price_td_el = ("//table[@id='standardRatesTable']"
                             "//tr[1]/td[2]")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def close(self):
        self.driver.close()

    def check_price_for(self, country_name):
        self.country_input.clear()
        self.country_input.send_keys(country_name)
        self.country_input.send_keys(Keys.RETURN)

        try:
            WebDriverWait(self.driver, self._ajax_load_timeout).until(
                EC.presence_of_element_located((
                    By.XPATH,
                    self._ajax_loaded_el % country_name)
                )
            )
        except TimeoutException:
            raise O2PriceInspectorException(("Country %s doesn't exist, "
                                             "or HTML structure changed.")
                                             % country_name)

        try:
            standard_rates_price = self.driver.find_element(
                By.XPATH,
                self._price_td_el
            )
        except NoSuchElementException:
            raise O2PriceInspectorException("Price el can not be found "
                                            "HTML structure changed.")

        return Decimal(
            standard_rates_price.get_attribute(
                'innerText'
            ).encode('ascii', errors='ignore')
        )
