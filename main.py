#!/usr/bin/python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from selenium.common.exceptions import NoSuchElementException

from decimal import Decimal


countries = [
    "Canada",
    "Germany",
    "Iceland",
    "Pakistan",
    "Singapore",
    "South Africa"
]

driver = webdriver.Chrome()
driver.get("http://international.o2.co.uk/internationaltariffs/calling_abroad_from_uk")

country_input = driver.find_element_by_id("countryName")

for country_name in countries:

    country_input.clear()
    country_input.send_keys(country_name)
    country_input.send_keys(Keys.RETURN)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((
            By.XPATH,
            "//div[@id='paymonthlyTariffPlan']//h2[text()[contains(.,'%s')]]" % country_name)
        )
    )
    
    standard_rates_cost = driver.find_element(By.XPATH, "//table[@id='standardRatesTable']//tr[1]/td[2]")
    price_txt = standard_rates_cost.get_attribute('innerText')
    price = Decimal(price_txt.encode('ascii', errors='ignore'))

    print country_name, price

driver.close()
