class Account:

    OVERDRAFT_FEE = 35.00
    MAX_OVERDRAFT_LIMIT = -100.00
    MAX_WITHDRAWAL_WHEN_NEGATIVE = 100.00
    MAX_OVERDRAFTS_ALLOWED = 2


    def __init__(self, account_id: int, balance_checking: float, balance_saving: float, 
                 overdraft_count = 0, active = True):
        self.account_id = account_id
        self.balance_checking = balance_checking
        self.balance_saving = balance_saving
        self.active = active   
        self.overdraft_count = overdraft_count  

    def deposit_checking(self, amount: float):
        if amount <=0:
            print("Deposit amount must be more than 0.")
            return False
        self.balance_checking += amount
        return True

 
    def deposit_savings(self, amount: float):
        if amount <= 0:
            print("Deposit amount must be more than 0.")
            return False
        self.balance_saving += amount
        return True
    

    def withdraw_checking(self, amount: float):
        if not self.active:
            print("Account is deactivated due to multiple overdrafts.")
            return False
        if amount <= 0:
            print("Withdrawal amount must be more than 0.")
            return False
        if self.balance_checking < 0 and amount > self.MAX_WITHDRAWAL_WHEN_NEGATIVE:
            print(f"Cannot withdraw more than ${self.MAX_WITHDRAWAL_WHEN_NEGATIVE} when balance is negative.")
            return False
        if (self.balance_checking - amount) < self.MAX_OVERDRAFT_LIMIT:
            print(f"This transaction would exceed the overdraft limit of ${self.MAX_OVERDRAFT_LIMIT}.")
            return False
        
        was_positive = self.balance_checking >= 0  # balance 50 SAR True
        self.balance_checking -= amount  # 60  balance = -10 SAR
        is_negative = self.balance_checking < 0  # - 10 < 0  True

        if was_positive and is_negative: #( True and False ) False  
            print("Applying overdraft fee.")
            self.balance_checking -= self.OVERDRAFT_FEE  # -10 -35 = -45
            self.overdraft_count += 1  # overdraft_count 0 +1 = 1
            if self.overdraft_count >= self.MAX_OVERDRAFTS_ALLOWED:
                self.deactivate()
                print("Account has been deactivated due to excessive overdrafts.")
        return True
    
    def withdraw_savings(self, amount: float):
        if amount <= 0:
            print("Withdrawal amount must be more than 0.")
            return False
        if amount > self.balance_saving:
            print("Insufficient funds in savings account.")
            return False
        self.balance_saving -= amount
        return True


    def transfer_from_checking_to_savings(self, amount: float):
        if amount <= 0:
            print("Transfer amount must be more than 0.")
            return False
        if self.balance_checking >= amount:
            self.balance_checking -= amount
            self.balance_saving += amount
            print("Transfer successful.")
            return True
        else:
            print("Insufficient funds in checking account for this transfer.")
            return False

    def transfer_from_savings_to_checking(self, amount: float):
        if amount <= 0:
            print("Transfer amount must be more than 0.")
            return False
        if self.balance_saving >= amount:
            self.balance_saving -= amount
            self.balance_checking += amount
            print("Transfer successful.")
            return True
        else:
            print("Insufficient funds in savings account for this transfer.")
            return False

    def deactivate(self):
        self.active = False
