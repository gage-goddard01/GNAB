# Name: GNAB_storage

# Purpose: This module contains all the functions needed so that the GNAB application
# can have persistent storage. SQLite will be the primary storage system. The application will 
# be able to import and export CSV files. 

# GNAB monetary conventions:
# All stored monetary amounts use integer cents.
# Positive transactions increase account balances.
# Negative transactions decrease account balances.
# Credit card debt is represented by a negative balance.

from pathlib import Path
import pandas as pd
import sqlite3
from decimal import Decimal, InvalidOperation

# Data storage directory
DATA_DIR = Path(__file__).resolve().parent / "data"

BUDGET_FILE = DATA_DIR / "budget.csv"
TRANSACTIONS_FILE = DATA_DIR / "all_transactions.csv"



# Database Connection
DB_FILE = DATA_DIR / "gnab.db"

def get_connection():
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    connection = sqlite3.connect(DB_FILE)
    connection.execute("PRAGMA foreign_keys = ON")

    return connection

# Initialize Database
def initialize_database():
    connection = get_connection()

    # Create Accounts Table
    try:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS accounts (
                account_id INTEGER PRIMARY KEY,
                nickname TEXT NOT NULL UNIQUE,
                account_type TEXT NOT NULL
                    CHECK (account_type IN (
                        'checking',
                        'savings',
                        'credit_card'
                    )),
                opening_balance_cents INTEGER NOT NULL
            )
        """)

        connection.commit()
   
    # Create Budget Groups Table
        connection.execute("""
            CREATE TABLE IF NOT EXISTS budget_groups (
                group_id INTEGER PRIMARY KEY,
                group_name TEXT NOT NULL UNIQUE
            )
        """)

        connection.commit()
    # Create Budget Categories Table
        connection.execute("""
            CREATE TABLE IF NOT EXISTS budget_categories (
                category_id INTEGER PRIMARY KEY,
                group_id INTEGER NOT NULL,
                category_name TEXT NOT NULL,

                FOREIGN KEY (group_id)
                    REFERENCES budget_groups(group_id)
                UNIQUE (group_id, category_id)
                )
            """)
    
        connection.commit()

    # Create Budget Allocations Table
        connection.execute("""
            CREATE TABLE IF NOT EXISTS budget_allocations (
            allocation_id INTEGER PRIMARY KEY,
            category_id INTEGER NOT NULL,
            budget_month TEXT NOT NULL,
            allocated_amount_cents INTEGER NOT NULL
                CHECK (allocated_amount_cents >= 0),

            FOREIGN KEY (category_id)
                REFERENCES budget_categories(category_id),
            UNIQUE (category_id, budget_month)
            )
        """)
    finally:
        connection.close()
        
# Load Transactions from Database

def load_transactions():
    connection = get_connection()

    try:
        all_transactions = pd.read_sql_query(
            "SELECT * FROM transactions",
            connection
        )

        return all_transactions

    finally:
        connection.close()

# Take all dollar amounts as strings and convert them to integer cents

def dollars_to_cents(amount):
    try:
        dollars = Decimal(amount.strip())
    except (InvalidOperation, AttributeError):
        raise ValueError("Invalid monetary amount.")

    if not dollars.is_finite():
        raise ValueError("Amount must be finite.")

    cents = dollars * 100

    if cents != cents.to_integral_value():
        raise ValueError("Amount cannot exceed two decimal places.")

    return int(cents)
