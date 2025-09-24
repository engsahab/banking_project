import unittest
from Bank.customer import Customer
from Bank.account import Account

class TestCustomer(unittest.TestCase):
    def test_create_customer(self):
        account = Account(account_id=1001)
        customer = Customer(customer_id=1, first_name="Sahab", last_name="Alharbi", password="s@123" ,account=account)
        self.assertEqual(customer.customer_id, 1)
        self.assertEqual(customer.first_name, "Sahab")
        self.assertEqual(customer.last_name, "Alharbi")
        self.assertEqual(customer.password, "s@123")
        self.assertIsNotNone(customer.account)

    def test_full_name_and_password(self):
        account = Account(account_id=2002)
        customer = Customer(customer_id=2, first_name="Noura", last_name="Abdullah", password="p@ss", account=account)
        self.assertEqual(customer.full_name(), "Noura Abdullah")
        self.assertTrue(customer.verify_password("p@ss"))
        self.assertFalse(customer.verify_password("wrong"))

if __name__ =="__main__":
    unittest.main()