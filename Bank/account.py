# Represents a bank account for a customer
class Account:
    def __init__(self, account_id, balance_checking=0, balance_savings=0):
        self.account_id = account_id              
        self.balance_checking = balance_checking  
        self.balance_savings = balance_savings   

    # Deposit money into checking or savings
    def deposit(self, amount, account_type):
        if account_type == "checking":
            self.balance_checking += amount
        elif account_type == "savings":
            self.balance_savings += amount
        else:
            raise ValueError("Invalid account type")

     # Withdraw money from checking or savings with overdraft protection
    def withdraw(self, amount, account_type):
        if not self.active:
            raise ValueError("Account is deactivated due to overdrafts.")       
        balance = getattr(self, f"balance_{account_type}")
        if balance - amount < -100:
            raise ValueError("Cannot withdraw: would exceed overdraft limit of -100")
        if balance - amount < 0:
            self.overdraft_count += 1
            setattr(self, f"balance_{account_type}", balance - amount - 35)
            print("Overdraft fee $35 applied")
            if self.overdraft_count >= 2:
                self.active = False
        else:
            setattr(self, f"balance_{account_type}", balance - amount)

    # Transfer money between checking and savings
    def transfer(self, amount, from_account, to_account):
        if from_account == "checking" and to_account == "savings":
            if amount <= self.balance_checking:
                self.balance_checking -= amount
                self.balance_savings += amount
            else:
                raise ValueError("Insufficient funds in checking")
        elif from_account == "savings" and to_account == "checking":
            if amount <= self.balance_savings:
                self.balance_savings -= amount
                self.balance_checking += amount
            else:
                raise ValueError("Insufficient funds in savings")
        else:
            raise ValueError("Invalid account types")
