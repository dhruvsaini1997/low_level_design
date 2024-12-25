import unittest

from src.encapsulation import BankAccount


class BankAccountTest(unittest.TestCase):

    def setUp(self):
        self.dhruv_account = BankAccount(123456789, 100, 'Bank of India')

    def test_balance(self):
        self.assertEqual(self.dhruv_account.get_balance(),100)

    def test_private(self):
        self.assertEqual(self.dhruv_account.get_account_number(), 123456789)

if __name__ == '__main__':
    unittest.main()