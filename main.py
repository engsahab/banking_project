from Bank.csv_bank import Bank
from Bank.customer import Customer
from Bank.account import Account

def run_customer_session(bank, customer_account):
    while True:
        print("\n--- Customer Menu ---")
        print(f"Checking Balance: ${customer_account.balance_checking:,.2f}")
        print(f"Savings Balance:  ${customer_account.balance_savings:,.2f}")
        print("1. Deposit to Checking")
        print("2. Deposit to Savings")
        print("3. Withdraw from Checking")
        print("4. Withdraw from Savings")
        print("5. Transfer from Checking to Savings")
        print("6. Transfer from Savings to Checking")
        print("7. Logout")
        
        choice = input("Enter your choice: ")

