# GNABv1_functions

# Module Containing Functions for GNABv1

# This module is divided into 3 sections: Initialization,  Management and Main Menu. The first covers functions needed
# for loading DataFrames and collecting information. The second includes functions for the daily management and
# use of the application. The third section is the main menu to customize and interact with the budget. 

# imports
import pandas as pd
import time
import math

# ===========================================================
# =========================SECTION 1=========================
# ===========================================================

# Import transactions from csv
def import_transactions_from_csv():
      pass

# Collect Banking Info--Also creates ready to allocate variable 
# This info gets put into a reusable dictionary
def collect_banking_info():
    bank_name = input("Enter your bank's name: ")
    account_name = input("Enter an account nickname: ")
    bank_account_balance = float(input("Enter the starting balance: "))
    

    # Create ready to allocate variable and make initial account balance the ready to allocate
    
    ready_to_allocate = bank_account_balance
    bank_info_dict = dict(bank_name=bank_name, account_name=account_name, bank_account_balance=bank_account_balance)

    # collected info gets returned with this function is called
    return bank_info_dict



# Display Banking Info
def display_banking_info(bank_name, account_name, bank_account_balance):
    print()
    print("----------------------------------")
    print("Bank Name:", bank_name)
    print("Account Nickname:", account_name)
    print("Account Balance: $", bank_account_balance)
    print("----------------------------------")
    print()

# Initialize Transactions DataFrame
def create_transactions_df():
    all_transactions_df =pd.DataFrame({
            "Group": [],
            "Date": [],
            "Account": [],
            "Category": [],
            "Payee": [],
            "Memo": [],
            "Amount": []
                    })
    return all_transactions_df
    
# Convert all_transactions DataFrame to re-usable CSV
def all_transactions_df_to_CSV():   
    all_transactions.to_csv("all_transactions.csv", index=False)

# Load CSV data into Python all_transactions DataFrame
    def load_all_transactions_csv_into_df():
        all_transactions = pd.read_csv("all_transactions.csv")
        return all_transactions
    
# Create Default Budget
def create_default_budget(dictionary):
    print()
    print("Here is the default budget...")
    print()
   
    budget = pd.DataFrame({
        "Group": ["Giving", "Immediate Obligations", "Immediate Obligations", "Immediate Obligations", "True Expenses", "Savings"],
        "Category": ["Tithe", "Housing", "Groceries", "Transportation","Replacement Car", "Emergency Fund"],
        "Budgeted": [(dictionary * .10), (dictionary * .18), (dictionary * .18),(dictionary * .18), (dictionary * .18), (dictionary * .18)],
        "Spent": [0.00, 0.00, 0.00, 0.00,0.00, 0.00],
                })

    budget["Category Balance"] = budget["Budgeted"] - budget["Spent"]
    print("=============================================")
    print()
    print(budget)
    print()
    print("=============================================")
    print()
    return budget

# Convert Budget DataFrame to CSV file for persistent storage

def make_budget_df_a_csv(budget):
    budget.to_csv("budget.csv", index=False)

# Load Budget CSV into usable Python DataFrame
def budget_csv_to_df():
    budget = pd.read_csv("budget.csv")

# Display Budget Function
def display_budget(budget):
    print()
    print("=============================================")
    print()
    print(budget)
    print()
    print("=============================================")
    print()

# Function to ensure that Budgeted Amount Never Exceeds Amount in Bank
def every_dollar_a_job(balance, budget):
    if balance < sum(budget["Budgeted"]):
        print('You budgeted more than you have in the bank!')
    elif balance > sum(budget["Budgeted"]):
        print("You have not given every dollar a job.")
    elif balance == sum(budget["Budgeted"]):
         print("You have given every dollar a job! Great job!!!")
    print()
     
     


# ===========================================================
# =========================SECTION 2=========================
# ===========================================================

# Enter transaction function
def enter_transaction():
    transaction_group = input("Enter the transaction group: ")
    transaction_category = input("Enter the transaction category: ")
    transaction_account = input("Enter the transaction account: ")
    transaction_payee = input("Enter the Payee: ")
    transaction_date = input("Enter the transaction date: ")
    transaction_memo = input("(Optional) Enter the transaction memo: ")
    transaction_amount = float(input("Enter the transaction amount: $"))

    all_transactions_df =pd.DataFrame({
                "Group": [transaction_group],
                "Category": [transaction_category],
                "Date": [transaction_date],
                "Account": [transaction_account],
                "Payee": [transaction_payee],
                "Memo": [transaction_memo],
                "Amount": [transaction_amount]
                        })
    
    print()
    print("=============================================")
    print()

# Display Transactions
def display_transactions(transactions):
      print(transactions)

# Adds/Subtracts transaction from banking total and display remainder
def run_transaction(bank_account_running_total, transaction_amount): 
	bank_account_running_total += transaction_amount
	print("New Bank Account Balance: $", bank_account_running_total)
	bank_account_running_total += transaction_amount
	return bank_account_running_total


# Adjust Value within DataFrame/Existing Budget- includes Data validation so program won't stop if user enters invalid data
def adjust_budget_value(budget):
    
    adjust_value_in_budget = "y"

    while adjust_value_in_budget == "y":
        
        # Collect Group and Category
        group = input("What is the category's Group that you want to edit?: ")
        category = input("What is the line item's Category that you want to edit?: ")
        
        # Find the correct row
        
        matching_row = (
            (budget["Group"] == group) &
            (budget["Category"] == category) 
            )
        
        # Validate Group and Category
        if not matching_row.any():
            print("")
            print("Group or category not found. Try again.")
            print()
            continue
        
        if matching_row.sum() > 1:
            print("Multiple matching categories found. Correct the duplicates.")
            return
        
        # Validate numerical input
        try:
            budgeted_amt = float(input("What do you want the new budgeted amount to be?: "))

        except ValueError:
            print("Invalid amount. Please enter a number.")
            continue
        if not math.isfinite(budgeted_amt) or budgeted_amt < 0:
            print("Enter a valid, non-negative amount.")
            continue
        budget.loc[matching_row, "Budgeted"] = budgeted_amt

        # Re calculate Category balance 
        budget.loc[matching_row, "Category Balance"] = (budget.loc[matching_row, "Budgeted"] - budget.loc[matching_row, "Spent"])
        print()
        print("Budget successfully updated!")
        print()
        # Ask the user if they want to adjust another category

        adjust_value_in_budget = input("Do you want to edit another category? (y/n): ")
        adjust_value_in_budget.strip().lower()
    display_budget(budget)
    

# ===========================================================
# =========================SECTION 3=========================
# ===========================================================


# Customize Budget Menu
def customize_budget_menu(budget):
    customize_budget = "y"
    while customize_budget == "y":
            print()
            print("=============================================")
            print("Customize Budget Menu")
            print("1. Add a new group/category/budget item")
            print("2. Enter a new transaction")
            print("3. Change Name for Group/Category or adjust values in budget")
            print("4. Display Budget")
            print("5. Display All Transactions")
            print("6. No changes")
            print("=============================================")
            print()
            try:
                custbudg_MainMenu_selection = int(input("Enter an option from the above menu: "))
            
            except ValueError: 
                print("Invalid Selection. Type 1, 2, 3, 4, 5 or 6.")
                print()
                continue

            if custbudg_MainMenu_selection not in (1, 2, 3, 4, 5, 6):
                print("Invalid Selection. Type 1, 2, 3, 4, 5 or 6.")
                print()
                continue
            elif custbudg_MainMenu_selection == 1:
                new_budget_item_group = input("Enter the name of your new budget category: ")
                new_budget_item_category = input("Enter the name of your new budget category: ")
                new_budget_item_amount = float(input("Allocate your category's budget an amount: $"))
                budget.loc[len(budget)] = [new_budget_item_group, new_budget_item_category, new_budget_item_amount, 0.00, new_budget_item_amount]
                display_budget(budget)
                time.sleep(2)
            elif custbudg_MainMenu_selection == 2:
                enter_transaction()
            elif custbudg_MainMenu_selection == 3:
                # Create Sub Menu for Main Menu option 3
                print("=============================================")
                print("OPTIONS:")
                print("1. Change the name of a Group or Category")
                print("2. Change the amount allocated to a category's budget")
                print("=============================================")
                
                # Initialize and validate Variable that contains user selection for submenu1 selection
                # User can only enter integer
                try:
                    custbudg_submenu1_selection = int(input("Enter an option from the above menu: "))
            
                except ValueError: 
                    print("Invalid Selection. Type 1 or 2.")
                    print()
                    continue
                
                # Validate the user only selects 1 or 2 from Submenu1 options
                if custbudg_submenu1_selection not in (1, 2):
                    print("Invalid Selection. Type 1 or 2.")
                    print()
                    continue
                
                # If statement for when user wans to change name of group or category
                if custbudg_submenu1_selection == 1:
                    print("You chose option 1.")

                # if statement for when user wants to change category's allocated amount
                if custbudg_submenu1_selection == 2:
                    adjust_budget_value(budget)

            elif custbudg_MainMenu_selection == 4:
                display_budget(budget)
            elif custbudg_MainMenu_selection == 5:
                display_transactions(all_transactions_df)
            elif custbudg_MainMenu_selection == 6:
                break
    print("-------------------------------")
    print(budget)
    print("-------------------------------")




# main function
def main():
	print("Null")
    
# Main Guard
if __name__ == "__main__":
    main()