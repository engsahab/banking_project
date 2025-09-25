from Bank.csv_bank import Bank
from Bank.customer import Customer
from Bank.account import Account

def run_customer_session(bank, customer_account):
    while True:
        print("\n Menu: ")
        print(f"Checking Balance: ${customer_account.balance_checking:,.2f}")
        print(f"Savings Balance:  ${customer_account.balance_savings:,.2f}")
        print("1. Deposit to Checking")
        print("2.Deposit to Savings.")
        print("3. Withdraw from checking ")
        print("4.Withdraw from Savings")
        print("5. Transfer from Checking to Savings")
        print("6. Transfer from Savings to Checking")
        print("7. Logout")
        
        choice = input("Enter your number: ")

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

def main():
    bank = Bank() 
    while True:
        print("\n--- Welcome to ACME Bank ---")
        print("1. Add New Customer")
        print("2. Login")
        print("3. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            try:
                first_name = input("Enter first name: ")
                last_name = input("Enter last name: ")
                password = input("Enter a new password: ")
                start_checking = float(input("Enter initial checking deposit: "))
                start_savings = float(input("Enter initial savings deposit: "))
                bank.add_customer(first_name, last_name, password, start_checking, start_savings)
            except ValueError:
                print("Invalid amount. Please enter a number for deposits.")

        elif choice == '2':
            account_id = input("Enter your account ID: ")
            password = input("Enter your password: ")
            
            customer = bank.authenticate(account_id, password)
            if customer:
                customer_account = bank.find_account(account_id)
                if not customer_account.active:
                    print("Your account is deactivated due to multiple overdrafts.")
                else:
                    print(f"\nWelcome, {customer.full_name()}!")
                    run_customer_session(bank, customer_account)
            else:
                print("Authentication failed. Please check your ID and password.")
        
        elif choice == '3':
            print("Thank you for using ACME Bank. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()