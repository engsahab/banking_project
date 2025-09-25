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
    
try:
            with open(self.filepath, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
    
                    customer = Customer(
                        account_id=row['account_id'],
                        first_name=row['first_name'],
                        last_name=row['last_name'],
                        password=row['password']
                    )
                    
                    account = Account(
                        account_id=row['account_id'],
                        balance_checking=float(row['balance_checking']),
                        balance_savings=float(row['balance_savings']),
                        overdraft_count=int(row.get('overdraft_count', 0)),
                        is_active=row.get('is_active', 'True') == 'True'
                    )
                    
                    self.customers[row['account_id']] = customer
                    self.accounts[row['account_id']] = account
        except FileNotFoundError:
            print("Info: bank.csv not found. A new one will be created upon saving.")
        except Exception as e:
            print(f"An error occurred while loading data: {e}")
