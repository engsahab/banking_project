from Bank.customer import Customer
from Bank.account import Account
import csv

class Bank:
    def _init_(self, filepath='bank.csv'):
        self.filepath = filepath
        self.customers = {}  # key: account_id, value: Customer instance
        self.accounts = {}   # key: account_id, value: Account instance
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
                        active=row.get('active', 'True') == 'True'
                    )
                    self.customers[row['account_id']] = customer
                    self.accounts[row['account_id']] = account
        except FileNotFoundError:
            print("Info: bank.csv not found. A new one will be created upon saving.")
        except Exception as e:
            print(f"An error occurred while loading data: {e}")

    def save_data(self):
        try:
            with open(self.filepath, mode='w', newline='') as file:
                header = [
                    'account_id', 'first_name', 'last_name', 'password',
                    'balance_checking', 'balance_savings', 'overdraft_count', 'active'
                ]
                writer = csv.DictWriter(file, fieldnames=header)
                writer.writeheader()
                for account_id in self.customers:
                    customer = self.customers[account_id]
                    account = self.accounts[account_id]
                    writer.writerow({
                        'account_id': customer.account_id,
                        'first_name': customer.first_name,
                        'last_name': customer.last_name,
                        'password': customer.password,
                        'balance_checking': account.balance_checking,
                        'balance_savings': account.balance_savings,
                        'overdraft_count': account.overdraft_count,
                        'active': account.active
                    })
        except Exception as e:
            print(f"An error occurred while saving data: {e}")

    def add_customer(self, first_name, last_name, password, start_checking, start_savings):
        new_id = self._generate_account_id()
        customer = Customer(new_id, first_name, last_name, password)
        account = Account(new_id, start_checking, start_savings)
        self.customers[new_id] = customer
        self.accounts[new_id] = account
        self.save_data()
        print(f"Customer {first_name} {last_name} added successfully with Account ID: {new_id}")
        return customer

    def _generate_account_id(self):
        if not self.customers:
            return '10001'  # starting account ID
        last_id = max([int(id) for id in self.customers.keys()])
        return str(last_id + 1)

    def find_account(self, account_id):
        return self.accounts.get(account_id)

    def authenticate(self, account_id, password):
        customer = self.customers.get(account_id)
        if customer and customer.verify_password(password):
            return customer
        return None