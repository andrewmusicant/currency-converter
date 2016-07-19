from currency import *

class CurrencyConverter:
    def __init__(self, rates):
        self.rates = rates

    def converter(self, from_currency , to_currency):
        if to_currency not in self.rates:
            raise UnknownCurrencyCodeError
        else:
            x = Currency(from_currency.amount * (self.rates[to_currency] /self.rates[from_currency.curr_code]), to_currency)
            return x

class UnknownCurrencyCodeError(Exception):
        pass


#CurrencyConverter.converter()
