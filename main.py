from Bank.csv_bank import Bank
from Bank.customer import Customer
from Bank.account import Account

def run_customer_session(bank, customer_account):
    while True:
        print("\n Menu : ")
        print(f"Checking Balance: ${customer_account.balance_checking:,.2f}")
        print(f"Saving Balance:  ${customer_account.balance_saving:,.2f}")
        print("1. Deposit to Checking")
        print("2. Deposit to Saving")
        print("3. Withdraw from Checking")
        print("4. Withdraw from Saving")
        print("5. Transfer from Checking to Saving")
        print("6. Transfer from Savings to Checking")
        print("7. Logout")

        choice = input("your choice : ")
        try:
            if choice == '1':
                amount = float(input("amount to deposit into checking "))
                if customer_account.deposit_checking(amount):
                    bank.save_data()
            elif choice == '2':
                amount = float(input(" amount to deposit into saving"))
                if customer_account.deposit_saving(amount):
                    bank.save_data()
            elif choice == '3':
                amount = float(input(" amount to withdraw from checking "))
                if customer_account.withdraw_checking(amount):
                    bank.save_data()
            elif choice == '4':
                amount = float(input(" amount to withdraw from saving "))
                if customer_account.withdraw_saving(amount):
                    bank.save_data()
            elif choice == '5':
                amount = float(input("  amount to transfer to saving "))
                if customer_account.transfer_from_checking_to_saving(amount):
                    bank.save_data()
            elif choice == '6':
                amount = float(input(" amount to transfer to checking "))
                if customer_account.transfer_from_saving_to_checking(amount):
                    bank.save_data()
            elif choice == '7':
             print("logine ")
             break
            else:
                print(" invalid choice  please try again ")
        except ValueError:
            print("invalid input Please enter a valid number for amout ")

def main():
    bank = Bank()
    while True:
        print("\n Welcome ")
        print("1 add new customer")
        print("2 login")
        print("3 exit")

        choice = input(" your choice: ")
        if choice == '1':
            try:
                first_name = input(" first name ")
                last_name = input(" last name ")
                password = input(" password ")
                start_checking = float(input(" checking deposit "))
                start_savings = float(input("  savings deposit "))
                bank.add_customer(first_name, last_name, password, start_checking, start_savings)
            except ValueError:
                print("invalid amout Please enter a number for deposit ")

        elif choice == '2':
            account_id = input("  your id ")
            password = input(" your password ")
            customer = bank.authenticate(account_id, password)
            if customer:
                customer_account = bank.find_account(account_id)
                if not customer_account.active:
                    print("your account is deactivated due to multiple overdrft ")
                else:
                    print(f"\nWelcome, {customer.full_name()}!")
                    run_customer_session(bank, customer_account)
            else:
                print(" failed please check your id and password.")

        elif choice == '3':
            print(" Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__== "__main__":
    main()