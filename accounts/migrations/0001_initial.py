# Generated by Django 4.2.14 on 2024-08-12 14:21

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        # This migration does not depend on any other migrations
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                # IBAN field with unique constraint and validation for correct format
                ('iban', models.CharField(
                    max_length=34, 
                    unique=True, 
                    validators=[
                        django.core.validators.RegexValidator(
                            message='IBAN must be in the correct format', 
                            regex='^[A-Z]{2}\\d{2}[A-Z0-9]{1,30}$'
                        )
                    ]
                )),
                # Balance field with default value of 0 and up to 15 digits, 2 decimal places
                ('balance', models.DecimalField(
                    decimal_places=2, 
                    default=0, 
                    max_digits=15
                )),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                # Date field that auto-populates with the current date and time when a transaction is created
                ('date', models.DateTimeField(auto_now_add=True)),
                # Amount field with validation for non-negative values, up to 15 digits, 2 decimal places
                ('amount', models.DecimalField(
                    decimal_places=2, 
                    max_digits=15, 
                    validators=[
                        django.core.validators.MinValueValidator(0)
                    ]
                )),
                # Transaction type field with choices for Deposit, Withdrawal, and Transfer
                ('transaction_type', models.CharField(
                    choices=[('D', 'Deposit'), ('W', 'Withdrawal'), ('T', 'Transfer')],
                    max_length=1
                )),
                # ForeignKey linking the transaction to an account with a cascade delete behavior
                ('account', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, 
                    related_name='transactions', 
                    to='accounts.account'
                )),
            ],
        ),
    ]
