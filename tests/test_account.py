import unittest
from Bank.account import Account
class TestAccount(unittest.TestCase):

    def test_create_account(self):
        account = Account(account_id=1001, balance_checking=500, balance_savings=1000)
        self.assertEqual(account.account_id, 1001)
        self.assertEqual(account.balance_checking, 500)
        self.assertEqual(account.balance_savings, 1000)
        self.assertTrue(account.active,True)
        self.assertEqual(account.overdraft_count, 0)

    def test_deposit(self):
        account = Account(account_id=1001)
        account.deposit(200, "checking")
        self.assertEqual(account.balance_checking, 200)
        account.deposit(300, "savings")
        self.assertEqual(account.balance_savings, 300)

    def test_withdraw_normal(self):
        account = Account(account_id=1001, balance_checking=500)
        account.withdraw(200, "checking")
        self.assertEqual(account.balance_checking, 300)

    def test_transfer(self):
        account = Account(account_id=1001, balance_checking=500, balance_savings=100)
        account.transfer(200, "checking", "savings")
        self.assertEqual(account.balance_checking, 300)
        self.assertEqual(account.balance_savings, 300)

    def test_overdraft(self):
        account = Account(account_id=1001, balance_checking=50)
        account.withdraw(70, "checking")  
        self.assertEqual(account.balance_checking, -55)
        self.assertEqual(account.overdraft_count, 1)
        self.assertTrue(account.active)

        account.withdraw(40, "checking") 
        self.assertFalse(account.active)
        self.assertEqual(account.overdraft_count, 2)

if __name__ == "__main__":
    unittest.main()