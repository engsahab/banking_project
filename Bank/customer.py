# Represents a bank customer 
from Bank.account import Account

class Customer:
    def __init__(self,  account_id, first_name, last_name, password):
        self.account_id = account_id
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
    
    def full_name(self):
         return f"{self.first_name} {self.last_name}"
    
    def verify_password(self,password_to_check):
            return self.password == password_to_check
