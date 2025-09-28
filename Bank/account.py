class Account:
 
 # These are the constants
    overedraft_fee = 35.00
    max_overdraft_limt = -100.00
    max_withdraw_if_negative = 100.00
    overdrsft_attempts = 2

    def __init__(self, account_id: int, balance_checking: float, balance_saving: float, 
                 overdraft_count = 0, active = True):
        self.account_id = account_id
        self.balance_checking = balance_checking
        self.balance_saving = balance_saving
        self.active = active   
        self. overdraft_count= overdraft_count  
        
#debosit
    def deposit_checking(self, amount: float):
        if amount <= 0:                               # if the deposiit amount is lees 0 the proocess will stop
            print("Deposit amount must be more than 0.")
            return False
        self.balance_checking += amount               # if it is great than 0 take the balance and add it to the exiting amounnt
        return True

    def deposit_saving(self, amount: float):  
        if amount <= 0:                                # some prooses as checking
            print("Deposit amount must be more than 0.")
            return False
        self.balance_saving += amount                   # //
        return True
    
    # withdraw
    def withdraw_checking(self, amount: float):
     if not self.active:                               # if the acount is cancaelled due to execting the two attempts we will not be able to withdraw
        print("Account is deactivated due to multiple overdrafts.")
        return False

     if amount <= 0:                                  ## some prooses as deposit checking
        print("Withdrawal amount must be more than 0.")
        return False

     if self.balance_checking < 0 and amount > self.max_withdraw_if_negative:
        print(f"Cannot withdraw more than ${self.max_withdraw_if_negative} when balance is negative.")  # if the account balance is already negative, it checks if the withdrawal amount is within the allowed limit. You cannot withdraw more than max_withdraw_if_negative when the balance is negative.
        return False

     if (self.balance_checking - amount) < self.max_overdraft_limt:
        print(f"This transaction would exceed the overdraft limit of ${self.max_overdraft_limt}.")   #before subtracting the money, the function checks if this withdrawal will exceed the overdraft limit ( -100). If yes, the withdrawal stops
        return False

     balanse_before = self.balance_checking  # balance 50 SAR True
     self.balance_checking -= amount
     balanse_after = self.balance_checking < 0  # - 10 < 0  True                # if all previous checks pass, the function subtracts the withdrawal amount from the checking balance. It also stores the balance before and checks if it becomes negative after the withdrawal.

     if balanse_before >= 0 and balanse_after: #( True and True )  
        print("Applying overdraft fee")
        self.balance_checking -= self.overedraft_fee                       #if the balance changes from positive to negative, an overdraft fee is applied automatically and the overdraft count increases by 1.
        self.overdraft_count += 1
        if self.overdraft_count >= self.overdrsft_attempts:          # if the overdraft count reaches the maximum allowed (2), the account is deactivated to prevent further withdrawals
            self.deactivate()
     return True
    
    def withdraw_saving(self, amount: float):
        if amount <= 0:
            print(" Withdrawal amount must be more than 0")
            return False
        if amount > self.balance_saving:
            print(" Insufficient funds in saving account")
            return False
        self.balance_saving -= amount
        return True

    def transfer_from_checking_to_saving(self, amount: float):
        if amount <= 0:
            print(" transfer amount must be more than 0")
            return False
        if self.balance_checking >= amount:
            self.balance_checking -= amount
            self.balance_saving += amount
            return True
        else:
            print(" Insufficient funds in checking account for this transfer ")
            return False

    def transfer_from_saving_to_checking(self, amount: float):
        if amount <= 0:
            print(" transfer amount must be more than 0 ")
            return False
        if self.balance_saving >= amount:
            self.balance_saving -= amount
            self.balance_checking += amount
            return True
        else:
            print("Withdrawal amount must be more than 0 ")
            return False

    def deactivate(self):
        self.active = False