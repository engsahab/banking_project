import unittest
from Bank.account import Account

class TestAccount(unittest.TestCase):

    def test_create_account(self):
        account = Account(account_id=1001, balance_checking=500, balance_savings=1000)
        self.assertEqual(account.account_id, 1001)
        self.assertEqual(account.balance_checking, 500)
        self.assertEqual(account.balance_savings, 1000)

if __name__ == "__main__":
    unittest.main()