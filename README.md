# Bank Account API

Welcome to the **Bank Account API**, a Django REST framework project designed to manage bank accounts and transactions seamlessly. This API allows you to create, update, and manage bank accounts, perform financial transactions like deposits, withdrawals, and transfers, and access detailed transaction histories. Swagger documentation is included to facilitate easy testing and interaction with the API.

## 🚀 Features

- **Bank Account Management**: Create, retrieve, update, and delete bank accounts.
- **Transactions**:
  - Deposit money into an account.
  - Withdraw money from an account.
  - Transfer money between accounts.
  - View transaction history with filtering options.
- **Interactive API Documentation**: Swagger UI provides a user-friendly interface for exploring and testing API endpoints.

## 📋 Requirements

- Python 3.x
- Django 3.x or higher
- Django REST Framework
- drf-yasg for API documentation
- Faker for generating dummy data

## 🛠️ Installation

Follow these steps to set up the project locally:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Harib0475/code_sherpas_account_data_test_task.git
   cd code_sherpas_account_data_test_task
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply database migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Populate the database with dummy data**:
   ```bash
   python manage.py populate_data
   ```

6. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

7. **Access the API documentation**:
   Open your browser and navigate to `http://127.0.0.1:8000/swagger/` to explore the API using Swagger UI.

## 🔗 API Endpoints

### 🏦 Accounts

- **List Accounts / Create Account**
  - `GET /api/accounts/`
  - `POST /api/accounts/`

- **Retrieve / Update / Delete Account**
  - `GET /api/accounts/{id}/`
  - `PUT /api/accounts/{id}/`
  - `DELETE /api/accounts/{id}/`

### 💸 Transactions

- **Deposit Money**
  - `POST /api/accounts/{id}/deposit/`
  - Request Body:
    ```json
    {
      "amount": 100.0
    }
    ```

- **Withdraw Money**
  - `POST /api/accounts/{id}/withdraw/`
  - Request Body:
    ```json
    {
      "amount": 50.0
    }
    ```

- **Transfer Money**
  - `POST /api/accounts/transfer/`
  - Request Body:
    ```json
    {
      "from_iban": "IBAN123",
      "to_iban": "IBAN456",
      "amount": 200.0
    }
    ```

- **List Transactions with Filters**
  - `GET /api/accounts/{id}/transactions/?end_date=2024-12-31&ordering=-date&page=2&page_size=1&start_date=2024-01-01&transaction_type=D`

## 🧪 Running Tests

To ensure everything is working as expected, run the tests with the following command:
```bash
python manage.py test
```

## ⚙️ Management Commands

The project includes a custom management command to populate the database with dummy data. Run the following command to generate sample data:
```bash
python manage.py populate_data
```

## 📚 Acknowledgements

This project is built with the following amazing tools:
- **Django REST Framework** for the robust API backend.
- **drf-yasg** for the Swagger documentation.
- **Faker** for easily generating realistic dummy data.
