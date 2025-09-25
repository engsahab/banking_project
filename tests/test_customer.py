import unittest
from Bank.customer import Customer 

class TestCustomer(unittest.TestCase):

    def setUp(self):
        
        self.customer = Customer(
            account_id='10001',
            first_name='Sahab',
            last_name='Alharbi',
            password='S123'
        )

    def test_customer_initialization(self):

        self.assertEqual(self.customer.account_id, '10001')
        self.assertEqual(self.customer.first_name, 'Sahab')
        self.assertEqual(self.customer.last_name, 'Alharbi')
        self.assertEqual(self.customer.password, 'S123')

    def test_full_name(self):
        self.assertEqual(self.customer.full_name(), 'Sahab Alharbi')

    def test_verify_password_correct(self):
        
        self.assertTrue(self.customer.verify_password('S123'))

    def test_verify_password_incorrect(self):
        self.assertFalse(self.customer.verify_password('wrongpassword'))


if __name__ == '__main__':
    unittest.main()