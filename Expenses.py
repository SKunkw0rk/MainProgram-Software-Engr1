# User Story 5: As a user I want to input and categorize my expenses so that I know if I am within my budget bucket through an alert.


'''
    This module contains the Expense class which is used to represent an expense with its details such as category, amount, and date. 

'''

import json

File_name= 'Expenses.json'


class ExpenseTracker:
    def __init__(self):

        self.categories = ['Gas', 'Food', 'Rent', 'Utilities', 'Entertainment', 'Miscellaneous']    # List of possible expense categories
        self.expenses = [] # List to store all expenses
        self.current_category = ''

        self.new_category = ''
        self.amount = 0.0
        self.descript = ''

        self.load_expenses()


    def menu_options(self):

        print('')
        print('1: Add expense')
        print('2: View expenses')
        print('3: Return to main page')

    def select_category(self):
        '''
            This method's functionality allows the user to select expense categories.
        '''

        print('Select a category: ')
        num = 1

        for ctgry in self.categories:
            print(str(num) + '. ' + ctgry)
            num = num + 1
        print(str(num) + '. Create a new category')
        print(str(num + 1) + '. Quit')

        usr_selects = int(input('Enter category number: '))

        if usr_selects == num + 1:
            self.current_category = ''
            print('Operation Cancelled')
        elif usr_selects == num:
            self.new_category = input('New category: ')
            self.categories.append(self.new_category)
            self.current_category = self.new_category
            print('Selected Category: ' + self.current_category)
        else:
            self.current_category = self.categories[usr_selects - 1]
            print('Selected Category: ' + self.current_category)


    def add_expense(self):
        '''
            This methods functionality is to let the user add expenses to a category. It saves this information in a dictionary which is then stored in a list.
        '''
        self.select_category()

        if self.current_category == '':
            return

        comma_amount = input('Amount: $')
        self.amount = float(comma_amount.replace(',',''))
        self.descript = input('Description: ')

        expense = {'category': self.current_category, 'amount': self.amount, 'descript': self.descript}
        self.expenses.append(expense)

        self.save_expenses()

        print('Expense added')
        print(('Category: ' + self.current_category))
        print('Amount: $' + str(self.amount))
        print('Description: ' + self.descript)
        print('Information Saved!')

    def save_expenses(self):
        '''
            This methods functionality opens writes to a file to save the users data.
        '''
        file = open(File_name, 'w')
        json.dump(self.expenses, file)
        file.close()

    def load_expenses(self):
        '''
            This methods functionality is to load the data from the json file handling errors along the way. If a category does not exist, it will be appended to the list of categories.
        '''
        try:
            with open(File_name, 'r') as expense_file:
                self.expenses = json.load(expense_file)
        except FileNotFoundError:
            self.expenses = []
        except json.JSONDecodeError:
            self.expenses = []
        for expense in self.expenses:
            if expense['category'] not in self.categories:
                self.categories.append(expense['category'])

    def get_total_history(self, category):
        ''' 
            This methods functionality adds up the amount per category so the user can know how much they have spent
        '''
        total = 0
        for expense in self.expenses:
            if expense ['category'] == category:
                total = total + expense['amount']
        return total

    def display_expense(self):
        '''
         This methods functionality displays the expenses.
        '''
        print('Expenses History:')
        if len(self.expenses) == 0:
            print('No Expenses')
            return
        for expense in self.expenses:
            print(expense['category'] + ' - $' + str(expense['amount']) + ' - ' + expense['descript'])

    def program_process(self):
        '''
            This method runs the program
        '''
        process = True
        while process:
            self.menu_options()
            print('')
            user_opt =  input('Choose an option: ')

            if user_opt == '1':
                self.add_expense()
            elif user_opt == '2':
                self.display_expense()
            elif user_opt == '3':
                process = False
            else:
                print('Please choose an option ')



if __name__ == '__main__':
    money_tracker = ExpenseTracker()
    money_tracker.program_process() 
