import unittest
from Bank.account import Account 

class TestAccount(unittest.TestCase):
    def setUp(self):
        self.account = Account(account_id='10001', balance_checking=500.0, balance_savings=1000.0)

    def test_deposit_checking_positive_amount(self):
        self.account.deposit_checking(100)
        self.assertEqual(self.account.balance_checking, 600)

    def test_deposit_savings_positive_amount(self):
        self.account.deposit_savings(200)
        self.assertEqual(self.account.balance_savings, 1200)
    
    def test_deposit_negative_amount(self):
        result = self.account.deposit_checking(-50)
        self.assertFalse(result) 
        self.assertEqual(self.account.balance_checking, 500)

    def test_withdraw_checking_sufficient_funds(self):
        self.account.withdraw_checking(100)
        self.assertEqual(self.account.balance_checking, 400)

    def test_withdraw_savings_insufficient_funds(self):
        result = self.account.withdraw_savings(1100)
        self.assertFalse(result)
        self.assertEqual(self.account.balance_savings, 1000)

    
    def test_transfer_from_checking_to_savings(self):
        self.account.transfer_from_checking_to_savings(100)
        self.assertEqual(self.account.balance_checking, 400)
        self.assertEqual(self.account.balance_savings, 1100)

    def test_transfer_from_savings_insufficient_funds(self):
        result = self.account.transfer_from_savings_to_checking(2000)
        self.assertFalse(result)
        self.assertEqual(self.account.balance_savings, 1000)
        self.assertEqual(self.account.balance_checking, 500)

    def test_overdraft_fee_application(self):
        self.account.withdraw_checking(520) 
        self.assertEqual(self.account.balance_checking, -55)
        self.assertEqual(self.account.overdraft_count, 1)

    def test_exceeding_max_overdraft_limit(self):
        result = self.account.withdraw_checking(601) 
        self.assertFalse(result)
        self.assertEqual(self.account.balance_checking, 500)

    def test_deactivation_after_two_overdrafts(self):
        self.account.withdraw_checking(510) 
        self.assertEqual(self.account.balance_checking, -45)
        self.assertEqual(self.account.overdraft_count, 1)
        self.assertTrue(self.account.active)
        
        self.account.withdraw_checking(60) 
        self.assertEqual(self.account.balance_checking, -100)
        self.assertEqual(self.account.overdraft_count, 2)
        self.assertFalse(self.account.active) 

if __name__ == '__main__':
    unittest.main()
