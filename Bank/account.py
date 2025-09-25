class Account:

    OVERDRAFT_FEE = 35.00
    MAX_OVERDRAFT_LIMIT = -100.00
    MAX_WITHDRAWAL_WHEN_NEGATIVE = 100.00
    MAX_OVERDRAFTS_ALLOWED = 2

    def __init__(self, account_id: int, balance_checking: float, balance_savings: float, 
                 overdraft_count = 0, active = True):
        self.account_id = account_id
        self.balance_checking = balance_checking
        self.balance_savings = balance_savings
        self.active = active   
        self.overdraft_count = overdraft_count  

    def deposit_checking(self, amount: float):
        if amount <= 0:
            print("Error: Deposit amount must be more than 0.")
            return False
        self.balance_checking += amount
        return True

    def deposit_savings(self, amount: float):
        if amount <= 0:
            print("Error: Deposit amount must be more than 0.")
            return False
        self.balance_savings += amount
        return True
    
    def withdraw_checking(self, amount: float):
        if not self.active:
            print("Error: Account is deactivated because to multiple overdrafts.")
            return False
        if amount <= 0:
            print("Error: Withdrawal amount must be more than 0.")
            return False
        if self.balance_checking < 0 and amount > self.MAX_WITHDRAWAL_WHEN_NEGATIVE:
            print(f"Error: Cannot withdraw more than ${self.MAX_WITHDRAWAL_WHEN_NEGATIVE} when balance is negative.")
            return False
        if (self.balance_checking - amount) < self.MAX_OVERDRAFT_LIMIT:
            print(f"Error: This transaction would exceed the overdraft limit of ${self.MAX_OVERDRAFT_LIMIT}.")
            return False
        
        was_positive = self.balance_checking >= 0
        self.balance_checking -= amount
        is_negative = self.balance_checking < 0

        if was_positive and is_negative:
            print("Applying overdraft fee.")
            self.balance_checking -= self.OVERDRAFT_FEE
            self.overdraft_count += 1
            if self.overdraft_count >= self.MAX_OVERDRAFTS_ALLOWED:
                self.deactivate()
                print("Account has been deactivated due to excessive overdrafts.")
        return True
    
    def withdraw_savings(self, amount: float):
        if amount <= 0:
            print("Error: Withdrawal amount must be positive.")
            return False
        if amount > self.balance_savings:
            print("Error: Insufficient funds in savings account.")
            return False
        self.balance_savings -= amount
        return True
        
    def transfer_from_checking_to_savings(self, amount: float):
        if amount <= 0:
            print("Error: Transfer amount must be positive.")
            return False
        if self.balance_checking >= amount:
            self.balance_checking -= amount
            self.balance_savings += amount
            print("Transfer successful.")
            return True
        else:
            print("Error: Insufficient funds in checking account for this transfer.")
            return False

    def transfer_from_savings_to_checking(self, amount: float):
        if amount <= 0:
            print("Error: Transfer amount must be positive.")
            return False
        if self.balance_savings >= amount:
            self.balance_savings -= amount
            self.balance_checking += amount
            print("Transfer successful.")
            return True
        else:
            print("Error: Insufficient funds in savings account for this transfer.")
            return False

    def deactivate(self):
        self.active = False
