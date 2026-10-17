#GNABv1 Pseudocode 

# Purpose: With limited AI help, construct a basic personal budgeting console application using python. Create reusable functions. Create a main() function that can perform calculations from user input. 

# Budget scope: 1 month

import pandas as pd
import GNABv1_functions as f
import importlib
import time
import math



# Misc
# bank_account_running_total = 
# ready_to_allocate = 


# Main(): Display welcome and menu // menu options include enter transaction (income or expense), enter amount in bank, plan expenses

def main():
    print("Welcome to GNABv1--A Budgeting Application!")
    print("We need to collect a lot of information to get started...")

    # Collect and store banking info into variables for later use (and create ready to allocte)
    # Also creates dictionary of banking information
    bank_info_dict = f.collect_banking_info()
    

    # Display Banking info 
    f.display_banking_info(bank_info_dict["bank_name"], bank_info_dict["account_name"], bank_info_dict["bank_account_balance"])
    time.sleep(2)

    # Intialize Transactions DataFrame
    f.create_transaction_DF()
    
    # Load Default Budget
    budget = f.create_default_budget(bank_info_dict["bank_account_balance"])
    time.sleep(1.5)
   
   # Run Every Dollar has a job function
    # f.every_dollar_a_job(budgetbank_account_balance, budget)

    # Customize Budget Main Menu
    f.customize_budget_menu(budget)
            




# Main Guard
if __name__ == "__main__":
    main()


