from currency_converter import *
from nose.tools import raises

dict_of_rates={'USD': 1.0, 'EUR': 0.74, 'GBP': 0.90, 'JPY': 120.0}


def test_currency_converter():
    assert CurrencyConverter(dict_of_rates).rates == dict_of_rates

def test_exchange_between_same_curr_code():
    assert CurrencyConverter(dict_of_rates).converter(Currency(3, 'USD'),'USD') == Currency(3, 'USD')

def test_exchange_between_different_curr_code():
    assert CurrencyConverter(dict_of_rates).converter(Currency(1, 'USD'),'JPY') == Currency(120, 'JPY')

def test_exchange_between_different_curr_code_2():
    assert CurrencyConverter(dict_of_rates).converter(Currency(1, 'EUR'),'JPY') == Currency(120/.74, 'JPY')

@raises(UnknownCurrencyCodeError)
def test_different_currency_codes_raises_error():
    CurrencyConverter(dict_of_rates).converter(Currency(1, 'EUR'),'ESP') #== Currency(120/.74, 'JPY')
