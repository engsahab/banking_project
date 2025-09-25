import csv
from Bank.customer import Customer
from Bank.account import Account

class Bank:
    def __init__(self, filepath='bank.csv'):
        self.filepath = filepath
        self.customers = {}  
        self.accounts = {}  
        self.load_data()

    def load_data(self):
    
