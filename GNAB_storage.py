# Name: GNAB_storage

# Purpose: This module contains all the functions needed so that the GNAB application
# can have persistent storage. SQLite will be the primary storage system. The application will 
# be able to import and export CSV files. 



from pathlib import Path
import pandas as pd
import sqlite3

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

    try:
        # Later, we'll create the SQLite tables here.
        pass

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

