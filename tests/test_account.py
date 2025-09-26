import unittest
from Bank.account import Account 

class TestAccount(unittest.TestCase):
    def setUp(self):
        self.account = Account(account_id='10001', balance_checking=500.0, balance_saving=1000.0)
    
    #test debosit
    def test_deposit_checking(self):
        self.account.deposit_checking(100)
        self.assertEqual(self.account.balance_checking, 600)

    def test_deposit_saving(self):
        self.account.deposit_saving(200)
        self.assertEqual(self.account.balance_saving, 1200)

    def test_deposit_negative_amount(self):
        result = self.account.deposit_checking(-50)
        self.assertFalse(result)
        self.assertEqual(self.account.balance_checking,500)

     #test withdrw
    def test_withdraw_checking_(self):
        self.account.withdraw_checking(100)
        self.assertEqual(self.account.balance_checking, 400)

    def test_withdraw_saving(self):
        result = self.account.withdraw_saving(1100)
        self.assertFalse(result)
        self.assertEqual(self.account.balance_saving, 1000)

# test transfer
    def test_transfer_from_checking_to_saving(self):
        self.account.transfer_from_checking_to_saving(100)
        self.assertEqual(self.account.balance_checking, 400)
        self.assertEqual(self.account.balance_saving, 1100)

    def test_transfer_from_saving_to_checing_insufficient(self):
        result = self.account.transfer_from_saving_to_checking(2000)
        self.assertFalse(result)
        self.assertEqual(self.account.balance_saving, 1000)
        self.assertEqual(self.account.balance_checking, 500)

# test overdraft
    def test_overedraft_fee_application(self):
        self.account.withdraw_checking(520) 
        self.assertEqual(self.account.balance_checking, -55)
        self.assertEqual(self.account.overdraft_count, 1)

    def test_exceeding_max_overdraft_limt(self):
        result = self.account.withdraw_checking(601) 
        self.assertFalse(result)
        self.assertEqual(self.account.balance_checking, 500)

    def test_deactivation_after_two_overdraft(self):
        self.account.withdraw_checking(510) 
        self.assertEqual(self.account.overdraft_count, 1)
        self.assertTrue(self.account.active)
        
        self.account.withdraw_checking(60) 
        self.assertEqual(self.account.overdraft_count, 2)
        self.assertFalse(self.account.active)
        
if __name__ == '__main__':
    unittest.main()