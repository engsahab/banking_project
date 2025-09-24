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

if __name__ =="__main__":
    unittest.main()

