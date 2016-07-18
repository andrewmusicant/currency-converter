#from currency_converter import converter

class Currency:
    def __init__(self,amount,curr_code):
        self.amount= amount
        self.curr_code= curr_code

    def __eq__(self, another_currency):
        return self.amount == another_currency.amount and \
        self.curr_code == another_currency.curr_code

    def __nq__(self, another_currency):
        return self.amount == another_currency.amount and \
        self.curr_code != another_currency.curr_code

    def __add__(self,second_curr):
        if self.curr_code == second_curr.curr_code:
            return Currency(self.amount + second_curr.amount, self.curr_code )
        else:
            raise DifferentCurrencyCodeError

    def __sub__(self,second_curr):
        if self.curr_code == second_curr.curr_code:
            return Currency(self.amount - second_curr.amount, self.curr_code )
        else:
            raise DifferentCurrencyCodeError

    def __mul__(self,second_curr):
        if self.curr_code == second_curr.curr_code:
            return Currency(self.amount * second_curr.amount, self.curr_code)
        else:
            raise DifferentCurrencyCodeError

class DifferentCurrencyCodeError(Exception):
    pass


# def main():
#     print("USD = $, or U.S. Dollar; EUR = €, or Euro")
#     print("GBP = £, or British Pound; JPY = ¥, or Yen")
#     EnteredValues={}
#     converter()
#     while True:
#         amount = input("Please enter the amount of currency: ")
#         curr_code = input("Please enter the country code you wish to use. See above for help: ")
#         str(curr_code)
#         curr_code_checker(curr_code)
#         EnteredValues[curr_code]= amount
#         print(EnteredValues)
#
# if __name__=='__main__':
#     main()
# def curr_code_checker(curr_code):
#     if curr_code == '$' or curr_code == 'USD' or curr_code == 'U.S. Dollar':
#         curr_code = 'USD'
#     elif curr_code == '€' or curr_code == 'EUR' or curr_code == 'Euro':
#         curr_code = 'EUR'
#     elif curr_code == '£' or curr_code == 'GBP' or curr_code == 'British Pound':
#         curr_code = 'GBP'
#     elif curr_code == '¥' or curr_code == 'JPY' or curr_code == 'Yen':
#         curr_code = 'JPY'
#     else:
#         print("Please enter a valid currency")
#
#
#
# def string_input(string):
#     special_char = list(string)
#     if special_char[0] == '$':
#         special_char[0] = 'USD'
#     elif special_char[0] == '€':
#         special_char[0] = 'EUR'
#     elif special_char[0] == '¥':
#         special_char[0] = 'JPY'
#     elif special_char[0] == '£':
#         special_char[0] = 'GBP'
#     amount = float(special_char[1:])
