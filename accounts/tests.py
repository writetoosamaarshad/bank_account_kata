from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Account, Transaction


class AccountTests(APITestCase):
    """
    Test suite for the Account and Transaction models' API endpoints.
    """

    def setUp(self):
        """
        Set up test data for the tests. 
        This method is run before each test case.
        """
        self.account = Account.objects.create(iban='US64SVBKUS6S3300958879', balance=1500.00)
        self.account2 = Account.objects.create(iban='FR1420041010050500013M02606', balance=300.00)

    def test_create_account(self):
        """
        Test creating a new account via the API.
        """
        url = reverse('account-list')
        data = {'iban': 'ES9121000418450200051332', 'balance': 2000.00}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_accounts(self):
        """
        Test retrieving a list of accounts via the API.
        """
        url = reverse('account-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Check if the correct number of accounts is returned

    def test_retrieve_account(self):
        """
        Test retrieving a single account by ID via the API.
        """
        url = reverse('account-detail', args=[self.account.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['iban'], self.account.iban)

    def test_update_account(self):
        """
        Test updating an account's balance via the API.
        """
        url = reverse('account-detail', args=[self.account.id])
        data = {'iban': self.account.iban, 'balance': 2500.00}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.account.refresh_from_db()
        self.assertEqual(self.account.balance, 2500.00)

    def test_delete_account(self):
        """
        Test deleting an account via the API.
        """
        url = reverse('account-detail', args=[self.account.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Account.objects.filter(id=self.account.id).exists())

    def test_deposit(self):
        """
        Test depositing money into an account via the API.
        """
        url = reverse('account-deposit', args=[self.account.id])
        data = {'amount': 750.00}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.account.refresh_from_db()
        self.assertEqual(self.account.balance, 2250.00)

    def test_withdraw(self):
        """
        Test withdrawing money from an account via the API.
        """
        url = reverse('account-withdraw', args=[self.account.id])
        data = {'amount': 500.00}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.account.refresh_from_db()
        self.assertEqual(self.account.balance, 1000.00)

    def test_withdraw_insufficient_funds(self):
        """
        Test withdrawing more money than the account balance, 
        which should fail with a 400 Bad Request.
        """
        url = reverse('account-withdraw', args=[self.account.id])
        data = {'amount': 2000.00}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_transfer(self):
        """
        Test transferring money between two accounts via the API.
        """
        url = reverse('account-transfer')
        data = {'from_iban': self.account.iban, 'to_iban': self.account2.iban, 'amount': 500.00}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.account.refresh_from_db()
        self.account2.refresh_from_db()
        self.assertEqual(self.account.balance, 1000.00)
        self.assertEqual(self.account2.balance, 800.00)

    def test_transfer_insufficient_funds(self):
        """
        Test transferring more money than available in the source account,
        which should fail with a 400 Bad Request.
        """
        url = reverse('account-transfer')
        data = {'from_iban': self.account.iban, 'to_iban': self.account2.iban, 'amount': 2000.00}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_list_transactions(self):
        """
        Test listing transactions for an account via the API.
        """
        Transaction.objects.create(account=self.account, amount=200.00, transaction_type=Transaction.DEPOSIT)
        url = reverse('transaction-list', args=[self.account.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Check if the correct number of transactions is returned

    def test_invalid_account_creation(self):
        """
        Test creating an account with an invalid IBAN, which should fail with a 400 Bad Request.
        """
        url = reverse('account-list')
        data = {'iban': 'INVALIDIBAN', 'balance': 1000.00}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_negative_balance_deposit(self):
        """
        Test depositing a negative amount into an account, which should fail with a 400 Bad Request.
        """
        url = reverse('account-deposit', args=[self.account.id])
        data = {'amount': -500.00}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
