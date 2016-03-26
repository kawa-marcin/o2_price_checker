# O2PriceInspector
Simple class, used to retrieve landline call rates to different countries for O2 network.

## Prerequisites
Class heavily depends on Selenium. To install easy all required packages run:

```
pip install -r requirements.txt
```

## Run example

```
$ git clone https://github.com/kawa-marcin/o2_price_inspector.git
$ cd o2_price_inspector
$ pip install -r requirements.txt
$
$ python main.py

Canada 1.00
Germany 1.00
Iceland 1.00
Pakistan 1.20
Singapore 1.00
South Africa 1.00

```

## Basic usage

```python
from o2_price_inspector import O2PriceInspector

if __name__ == '__main__':
  with O2PriceInspector() as price_inspector:
    country_name = 'Canada'
    price = price_inspector.check_price_for(country_name)

    print country_name, price
```