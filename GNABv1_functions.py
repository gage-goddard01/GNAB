# GNABv1_functions

# Module Containing Functions for GNABv1

# Import transactions from csv
def import_transactions_from_csv():
      pass

# Adds/Subtracts transaction from banking total and display remainder
def run_transaction(bank_account_running_total, transaction_amount): 
	bank_account_running_total += transaction_amount
	print("New Bank Account Balance: $", bank_account_running_total)
	bank_account_running_total += transaction_amount
	return bank_account_running_total
	

# Display Banking Info
def display_banking_info(bank_name, bank_account_number, bank_routing_number, bank_account_running_total):
	print("Bank Name:", bank_name)
	print("Account Number:", bank_account_number)
	print("Routing Number:", bank_routing_number)
	print("Account Balance: $", bank_account_running_total)

# main function
def main():
	print("Null")

# Enter transaction function
def enter_transaction():
    transaction_group = input("Enter the transaction group: ")
    transaction_category = input("Enter the transaction category: ")
    transaction_account = input("Enter the transaction account: ")
    transaction_payee = input("Enter the Payee: ")
    transaction_date = input("Enter the transaction date: ")
    transaction_memo = input("(Optional) Enter the transaction memo: ")
    transaction_amount = float(input("Enter the transaction amount: $"))


# Identify expenses/ list categories
def customize_budget():
    budget_group = input("Enter your budget group: ")
    budget_category = input("Enter your budget category: ")
    budget_category_amount = float(input("Assign your category's budget an amount: $"))

# Change Budgeted amount for existing category


# Change Spent amount for existing category

# Main Guard
if __name__ == "__main__":
    main()