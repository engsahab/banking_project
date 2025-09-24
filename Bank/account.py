class Account:
    def __init__(self, account_id, balance_checking=0, balance_savings=0):
        self.account_id = account_id
        self.balance_checking = balance_checking
        self.balance_savings = balance_savings
        self.active = True   
        self.overdraft_count = 0   

    def _ensure_valid_account_type(self, account_type):
        if account_type not in ("checking", "savings"):
            raise ValueError("Invalid account type")

    def _ensure_positive_amount(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")

    def deposit(self, amount, account_type):
        self._ensure_positive_amount(amount)
        self._ensure_valid_account_type(account_type)
        if account_type == "checking":
            self.balance_checking += amount
        elif account_type == "savings":
            self.balance_savings += amount

    def withdraw(self, amount, account_type):
        self._ensure_positive_amount(amount)
        self._ensure_valid_account_type(account_type)
        if not self.active:
            raise ValueError("Account is deactivated due to overdrafts.")

        balance = getattr(self, f"balance_{account_type}")
        projected_without_fee = balance - amount
        if projected_without_fee < -100:
            raise ValueError("Cannot withdraw: would exceed overdraft limit of -100")
        if projected_without_fee < 0:
            self.overdraft_count += 1
            print("Overdraft fee $35 applied")
            setattr(self, f"balance_{account_type}", projected_without_fee - 35)
            if self.overdraft_count >= 2:
                self.active = False
        else:
            setattr(self, f"balance_{account_type}", projected_without_fee)

    def transfer(self, amount, from_account, to_account):
        self._ensure_positive_amount(amount)
        self._ensure_valid_account_type(from_account)
        self._ensure_valid_account_type(to_account)
        if from_account == to_account:
            raise ValueError("from_account and to_account must be different")
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

    def get_balance(self, account_type):
        self._ensure_valid_account_type(account_type)
        return getattr(self, f"balance_{account_type}")

    def get_balances(self):
        return {
            "checking": self.balance_checking,
            "savings": self.balance_savings,
        }

    def reactivate(self):
        if self.balance_checking < 0 or self.balance_savings < 0:
            raise ValueError("Cannot reactivate: balances must be non-negative")
        self.active = True
        self.overdraft_count = 0