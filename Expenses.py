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

        invalid_input = False

        while not invalid_input:
            try:
                usr_selects = int(input('Enter category number: '))
                if usr_selects >= 1 and usr_selects <= num + 1:
                    invalid_input = True
                else:
                    print('Enter number between 1 and ' + str(num + 1) + '.')
            except ValueError:
                print('Please enter valid option.')

        if usr_selects == num + 1:
            self.current_category = ''
            print('Operation Cancelled')
        elif usr_selects == num:
            new_category = input('Enter a new category or type "back" to return to category listing: ').strip()

            while new_category == '':
                print('New category cannot be empty')
                new_category = input('Enter a new category or type "back" to return to category listing: ').strip()
            if new_category.lower() == 'back':
                self.select_category()
            else:
                self.new_category = new_category
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

        valid_expense = False # making sure the usr input is a vali number
        while not valid_expense:
            coma = input('Amount: $')
            try:
                self.amount = float(coma.replace(',', ''))
                if self.amount > 0 :
                    valid_expense = True
                else:
                    print('Amount must be greater than 0')
            except ValueError:
                print('Please enter valid amount')

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
            if expense['category'] != '' and expense['category'] not in self.categories: # skips empty categories
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
