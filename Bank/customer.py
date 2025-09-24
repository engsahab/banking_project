# Represents a bank customer 
from Bank.account import Account

class Customer:
    def __init__(self, customer_id, first_name, last_name, password, account=None):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.account = account 
    def full_name(self):
          return f"{self.first_name}{self.last_name}".strip()
    def verify_password(self,candidata_password):
            return self.password == candidata_password