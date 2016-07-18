from currency import *

class CurrencyConverter:
    def converter():
        dict={'USD': 1.0, 'EUR': 0.74, 'GBP': 0.90, 'JPY': 120.0}

        begin_curr_code = input("Please enter your starting Currency Code: ")
        curr_amount = input("Please enter the amount of money you wish to convert: ")
        end_curr_code = input("Pleasr enter the Currency you wish to convert to: ")

        value1 = dict[begin_curr_code]
        dict[begin_curr_code]= curr_amount
        value1=float(curr_amount)
        value2 = dict[end_curr_code]
        print("You have gone from", begin_curr_code, "to", end_curr_code, "your total is",value1 * value2)


CurrencyConverter.converter()
