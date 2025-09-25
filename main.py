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

 try:
            if choice == '1':
                amount = float(input("Enter amount to deposit into checking: "))
                if customer_account.deposit_checking(amount):
                    print("Deposit successful.")
                    bank.save_data()
            elif choice == '2':
                amount = float(input("Enter amount to deposit into savings: "))
                if customer_account.deposit_savings(amount):
                    print("Deposit successful.")
                    bank.save_data()
            elif choice == '3':
                amount = float(input("Enter amount to withdraw from checking: "))
                if customer_account.withdraw_checking(amount):
                    print("Withdrawal successful.")
                    bank.save_data()
            elif choice == '4':
                amount = float(input("Enter amount to withdraw from savings: "))
                if customer_account.withdraw_savings(amount):
                    print("Withdrawal successful.")
                    bank.save_data()
            elif choice == '5':
                amount = float(input("Enter amount to transfer to savings: "))
                if customer_account.transfer_from_checking_to_savings(amount):
                    bank.save_data() 
            elif choice == '6':
                amount = float(input("Enter amount to transfer to checking: "))
                if customer_account.transfer_from_savings_to_checking(amount):
                    bank.save_data() 
            elif choice == '7':
                print("Logging out...")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number for amounts.")
