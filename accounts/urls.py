from django.urls import path
from .views import AccountListCreateView, AccountDetailView, deposit, withdraw, transfer, TransactionListView

urlpatterns = [
    # URL pattern for listing all accounts or creating a new account
    path('accounts/', AccountListCreateView.as_view(), name='account-list'),

    # URL pattern for retrieving, updating, or deleting a specific account by its primary key (ID)
    path('accounts/<int:pk>/', AccountDetailView.as_view(), name='account-detail'),

    # URL pattern for depositing money into a specific account by its primary key (ID)
    path('accounts/<int:pk>/deposit/', deposit, name='account-deposit'),

    # URL pattern for withdrawing money from a specific account by its primary key (ID)
    path('accounts/<int:pk>/withdraw/', withdraw, name='account-withdraw'),

    # URL pattern for transferring money between accounts
    path('accounts/transfer/', transfer, name='account-transfer'),

    # URL pattern for listing all transactions for a specific account by its primary key (ID)
    path('accounts/<int:pk>/transactions/', TransactionListView.as_view(), name='transaction-list'),
]
