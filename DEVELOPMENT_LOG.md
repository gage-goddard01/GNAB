# GNAB Development Log

This document records my progress developing GNAB,
including completed features, programming concepts,
and architectural decisions.

## October 16, 2026

### Development Progress

1. Added groups column to budget DataFrame and default budget
2. Run enter_transaction() upon selecting main menu option 2
3. Customize budget menu became the main menu
4. Divided the functions module into 3 sections: functions for initialization of app, functions for management and use of app and finally the customize budget main menu function. 
5. Edited main() in GNABv1 so that it calls more functions from GNABv1_functions module and reduced amount of hard coding in GNABv1.py
6. Improved Customize Budget Menu (Which is a function)
7. Improved default budget so that it loads % of user’s initial banking balance

## October 17, 2026

### Development Progress

1. Created adjust_budget_value() so that a user can adjust budgeted amounts of categories in their budget. Called this function in GNABv1. Function includes input validation.
2. Changed language in code from “Ready to Assign” to “Ready to Allocate.” 
3. Created submenu1 within Customize Budget Main Menu function. It has 2 options. 1 changes the name of a group or category. 2 calls adjust_budget_value(). 
4. Changed collect_bank_info() so that it returns a dictionary of values rather than several variables.
5. Created prepare_banking_info() as core logic function that will be reusable for GUI and CLI.
6. Learned that the application doesn’t need Account and Routing numbers for eventual API integration. So, I removed those variables from collect_banking_info(). 

### Programming Concepts Practiced

- Python functions and modular programming
- Variable scope and passing arguments
- pandas DataFrame operations
- Input validation and exception handling
- Separating user interface code from application logic