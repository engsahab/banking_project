# Represents a bank account for a customer
class Account:
    def __init__(self, account_id, balance_checking=0, balance_savings=0):
        self.account_id = account_id
        self.balance_checking = balance_checking
        self.balance_savings = balance_savings