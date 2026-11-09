# User Story 5: As a user I want to input and categorize my expenses so that I know if I am within my budget bucket through an alert.


'''This module contains the Expense class which is used to represent an expense with its details such as category, amount, and date. 
    It also includes methods to categorize expenses and check if they are within the budget bucket. 
'''


categories = ['Gas', 'Food', 'Rent', 'Utilities', 'Entertainment', 'Miscellaneous']    # List of possible expense categories

expenses = [] # List to store all expenses

current_category = ''

def select_category():

    global current_category

    print('Select a category:')
    num = 1


    for ctgry in categories:
        print(str(num) + '. ' + ctgry)
        num = num + 1
    print(str(num) + '. Create a new category')


    usr_selects = int(input('Enter category number: '))

    if usr_selects == num:
        new_category = input('New category: ')
        categories.append(new_category)
        current_category = new_category
    else:
        current_category = categories[usr_selects - 1]
    print('Selected category: ' + current_category)

select_category()