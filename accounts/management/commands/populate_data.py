from django.core.management.base import BaseCommand
from accounts.models import Account, Transaction
from faker import Faker
import random


class Command(BaseCommand):
    """
    Django management command to populate the database with dummy data.
    This script generates dummy accounts and transactions for testing purposes.
    """

    help = 'Populate the database with dummy data'

    def handle(self, *args, **kwargs):
        """
        The entry point for the command.
        Creates dummy accounts and transactions.
        """
        faker = Faker()
        accounts = []

        # Create 10 dummy accounts with random IBANs and balances
        for _ in range(10):
            iban = faker.iban()
            balance = random.uniform(1000, 5000)
            account = Account.objects.create(iban=iban, balance=balance)
            accounts.append(account)

        transaction_types = [Transaction.DEPOSIT, Transaction.WITHDRAWAL, Transaction.TRANSFER]

        # Create random transactions for each account
        for account in accounts:
            for _ in range(random.randint(5, 15)):
                amount = random.uniform(10, 1000)
                transaction_type = random.choice(transaction_types)

                # Handle transfer transactions
                if transaction_type == Transaction.TRANSFER:
                    other_account = random.choice([acc for acc in accounts if acc != account])
                    Transaction.objects.create(account=account, amount=-amount, transaction_type=transaction_type)
                    Transaction.objects.create(account=other_account, amount=amount, transaction_type=transaction_type)
                    account.balance -= amount
                    other_account.balance += amount
                    account.save()
                    other_account.save()

                else:
                    # Handle deposit and withdrawal transactions
                    if transaction_type == Transaction.WITHDRAWAL and account.balance < amount:
                        amount = account.balance  # Prevent overdraft by setting amount to account balance
                    Transaction.objects.create(account=account, amount=amount, transaction_type=transaction_type)
                    if transaction_type == Transaction.DEPOSIT:
                        account.balance += amount
                    else:
                        account.balance -= amount
                    account.save()

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with dummy data'))
