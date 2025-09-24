# Represents a bank customer 
from Bank.account import Account

class Customer:
    def __init__(self, customer_id, first_name, last_name, password, account=None):

        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
<<<<<<< HEAD
        self.account = account 
=======
        self.account = account 
>>>>>>> 89bf6f5ee9668a1c1b320b7c625b6b4941107c78
