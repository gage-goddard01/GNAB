#GNABv1 Pseudocode 

# Purpose: With limited AI help, construct a basic personal budgeting console application using python. Create reusable functions. Create a main() function that can perform calculations from user input. 

# Budget scope: 1 month

import pandas as pd
import GNABv1_functions as f



# Misc
# bank_account_running_total = 
# ready_to_assign = 


# Main(): Display welcome and menu // menu options include enter transaction (income or expense), enter amount in bank, plan expenses

def main():
    print("Welcome to GNABv1--A Budgeting Application!")
    print("We need to collect a lot of information to get started...")

    # Collect Banking Info

    bank_name = input("Enter your bank’s name: ")
    bank_routing_number = int(input("Enter the bank account’s routing number: "))
    bank_account_number = int(input("Enter the bank account’s account number: "))
    bank_account_initial_amt = float(input("Enter the bank account’s initial amount: "))
    bank_account_running_total = bank_account_initial_amt

    # Display Banking info
    f.display_banking_info(bank_name, bank_routing_number, bank_account_number, bank_account_running_total)

    # Load Empty All Transactions DataFrame
    all_transactions = pd.DataFrame({
        # "Group": ["Immediate Obligations", "True Expenses", transaction_group ]
        "Date": [],
        "Account": [],
        "Category": [],
        "Payee": [],
        "Memo": [],
        "Amount": []
                })
    
    # Load Default Budget
    print()
    print("Here is the default budget...")
    print()
    budget = pd.DataFrame({
        "Category": ["Housing", "Groceries", "Transportation", "Savings"],
        "Budgeted": [1200.00, 400.00, 200.00, 300.00],
        "Spent": [0.00, 0.00, 0.00, 0.00],
                })

    budget["Category Balance"] = budget["Budgeted"] - budget["Spent"]

    print(budget)
    print()
    print("================")
    print()

    # Customize Budget Menu
    customize_budget = "y"
    while customize_budget == "y":
        print("Customize Budget Menu")
        print("1. Add a new category")
        print("2. Enter a new transaction")
        print("3. Change the budgeted amount for an existing category")
        print("4. Change the spent amount for an existing budgetcategory amount")
        print("5. Display Budget")
        print("6. No changes")
        print()
        try:
            cb_menu_selection = int(input("Enter an option from the above menu: "))
        
        except ValueError: 
            print("Invalid Selection. Type 1, 2, 3, 4 or 5.")
            print()
            continue

        if cb_menu_selection not in (1, 2, 3, 4, 5, 6):
            print("Invalid Selection. Type 1, 2, 3, 4, 5 or 6.")
            print()
            continue
        elif cb_menu_selection == 1:
            new_budget_category = input("Enter the name of your new budget category: ")
            new_budget_category_amount = float(input("Assign your category's budget an amount: $"))
            budget.loc[len(budget)] = [new_budget_category, new_budget_category_amount, 0.00, new_budget_category_amount]
        elif cb_menu_selection == 2:
            print("Selected 2")

        elif cb_menu_selection == 4:
            print(budget)
        elif cb_menu_selection == 5:
            break
    print(budget)
            




# Main Guard
if __name__ == "__main__":
    main()


