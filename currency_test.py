from currency import *
from nose.tools import raises

def test_create_currency_with_amount_and_code():
     one_dollar = Currency(1, 'USD')
     assert one_dollar.amount == 1
     assert one_dollar.curr_code == 'USD'

def test_currencys_can_be_equal():
    curr1 = Currency(99, 'USD')
    curr2 = Currency(99, 'USD')
    assert curr1 == curr2

def test_currencys_with_different_amounts_are_not_equal():
    curr1 = Currency(1, 'USD')
    curr2 = Currency(99, 'USD')
    assert curr1 != curr2

def test_currencys_with_different_currency_codes_are_not_equal():
    curr1 = Currency(1, 'USD')
    curr2 = Currency(1, 'EUR')
    assert curr1 != curr2

def test_adding_currencys_with_currency_codes_equal():
    curr1 = Currency(1, 'USD')
    curr2 = Currency(3, 'USD')
    assert curr1 + curr2 == Currency(4, 'USD')

def test_subtracting_currencys_with_currency_codes_equal():
    curr1 = Currency(6, 'USD')
    curr2 = Currency(3, 'USD')
    assert curr1 - curr2 == Currency(3, 'USD')

@raises(DifferentCurrencyCodeError)
def test_adding_different_currency_codes_raises_error():
    curr1 = Currency(6, 'USD')
    curr2 = Currency(3, 'EUR')
    curr1 + curr2

@raises(DifferentCurrencyCodeError)
def test_subtracting_different_currency_codes_raises_error():
    curr1 = Currency(6, 'USD')
    curr2 = Currency(3, 'EUR')
    curr1 - curr2

def test_multipling_currencys_with_currency_codes_equal():
    curr1 = Currency(6, 'USD')
    curr2 = Currency(5, 'USD')
    assert curr1 * curr2 == Currency(30, 'USD')
