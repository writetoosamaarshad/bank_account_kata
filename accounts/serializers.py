from rest_framework import serializers
from .models import Account, Transaction


class AccountSerializer(serializers.ModelSerializer):
    """
    Serializer for the Account model.

    This serializer provides the fields necessary to represent the 
    Account model in API responses and to handle data validation 
    and transformation during serialization/deserialization.
    """

    class Meta:
        model = Account
        fields = ['id', 'iban', 'balance']  # Fields to include in the serialized output


class TransactionSerializer(serializers.ModelSerializer):
    """
    Serializer for the Transaction model.

    This serializer handles the serialization and deserialization
    of Transaction instances, including validation of input data 
    and transformation to the desired output format.
    """

    class Meta:
        model = Transaction
        fields = ['id', 'account', 'date', 'amount', 'transaction_type']  # Fields to include in the serialized output
