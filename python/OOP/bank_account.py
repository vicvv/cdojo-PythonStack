
import datetime
from decimal import Decimal
from locale import currency, setlocale,LC_ALL
setlocale( LC_ALL, 'en_CA.UTF-8' )


class BankAccount:
    # class variables set here
    INITBALANCE = Decimal(0.0)
    MINIRATE = 0.01
    MAXIRATE = 2
    OVERDRAFT_FEES = Decimal(10.0)
    RATE = 0.02

    # constructor initialization

    def __init__(self, initial_rate=RATE,initial_balance=INITBALANCE):
        # local to instance _last_interest_date var used to determine applied date for interest
        self._last_interest_date = ''
        # setting balance and rate default setters in __init__
        self.rate = Decimal(initial_rate)if Decimal(initial_rate)> self.RATE else self.RATE
        self.balance = Decimal(initial_balance) if Decimal(initial_balance) > self.INITBALANCE else self.INITBALANCE

    # deposit method
    def deposit(self, input_amount):
        input_amount = self.valid_amount(input_amount)
        self.balance = self.balance + input_amount
        return self

    # withdraw method
    def withdrawal(self, input_amount):
        input_amount = self.valid_amount(input_amount)
        if self.balance < input_amount:
            self.balance = self.balance - BankAccount.OVERDRAFT_FEES - input_amount
            return self
        else:
            self.balance = self.balance - input_amount
            return self

    # balance getter
    def display_account_info(self):
        #return self.balance
        return currency(self.balance)

    # yield_interest method
    def yield_interest(self, rate):
        if self.validate_rate(rate) and self.balance > self.INITBALANCE:
            if not self._last_interest_date or \
                    datetime.date.today() > self._last_interest_date:
                self._last_interest_date = datetime.date.today()
                self.balance = self.balance * Decimal(1 + rate / 100)
                return self
            else:
                # return can be used to find out the next date to add interest
                self._last_interest_date + datetime.timedelta(20)
                return self

    # static method to validate the input_amount.
    @staticmethod
    def valid_amount(input_amount):
        if (isinstance(input_amount, float) or isinstance(input_amount, int)) \
                and input_amount > BankAccount.INITBALANCE:
            amount = Decimal(input_amount)
        else:
            amount = BankAccount.INITBALANCE
        return amount

    # class static method to validate the rate input
    @staticmethod
    def validate_rate(rate):
        try:
            if BankAccount.MINIRATE <= Decimal(rate) <= BankAccount.MAXIRATE:
                return Decimal(rate)
        except Exception as e:
            print(e)
            return False
            

vicky = BankAccount()
laura = BankAccount()
print(vicky.deposit(1000).deposit(70.25).deposit(10).withdrawal(40).yield_interest(1.5).display_account_info())
print(laura.deposit(2).deposit(7).withdrawal(4).withdrawal(20).withdrawal(23).withdrawal(40).display_account_info())
