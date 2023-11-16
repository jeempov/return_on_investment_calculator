import sys

class Property:
    def __init__(self, name):
        self.name = name
 
    # this function is a helper function to collect a numeric input for any value
    def get_input(prompt):
        value = None
        while value is None:
            try:
                user_input = input(prompt)
                if user_input.lower() == 'quit':
                    sys.exit()
                value = float(user_input)
            except ValueError:
                print('Please enter a valid number')
        return value
    
    # this function collects and prints income information
    def get_income(self):
        print("First, let's collect the income garnered from the property.")
        self.rental_income = Property.get_input('Please enter monthly rental income: ')
        self.laundry_income = Property.get_input('Please enter monthly laundry income: ')
        self.storage_income = Property.get_input('Please enter monthly storage income: ')
        self.miscellaneous_income = Property.get_input('Please enter monthly miscellaneous income: ')
        self.total_income = self.rental_income + self.storage_income + self.laundry_income + self.miscellaneous_income 
        print(f'Your total monthly income is: ${self.total_income}')
    
    # this function collects and prints expense information
    def get_expenses(self):
        print("You're doing great! Now, let's collect the expenses from the property.")
        self.insurance = Property.get_input("Please enter monthly insurance expenditures: ")
        self.utilities = Property.get_input("Please enter monthly utility expenditures: ")
        self.hoa = Property.get_input("Please enter monthly Homeowner Association Fees: ")
        self.lawn_snow = Property.get_input("Please enter monthly lawn or snow-related expenditures: ")
        self.vacancy = Property.get_input("Please enter monthly vacancy-related expenditures: ")
        self.repairs = Property.get_input("Please enter monthly repair-related expenditures: ")
        self.capital_expenditures = Property.get_input("Please enter monthly capital expenditures: ")
        self.property_management = Property.get_input("Please enter monthly property management expenditures: ")
        self.mortgage = Property.get_input("Please enter monthly mortgage expenditures: ")
        self.total_expenses = self.insurance + self.utilities + self.hoa + self.lawn_snow + self.vacancy + self.repairs + self.capital_expenditures + self.property_management + self.mortgage
        print(f'Your total monthly expenses are: ${self.total_expenses}')

    # this function calculates monthly and annual cash flow from the income and expense information collected
    def calc_cash_flow(self):
        self.monthly_cash_flow = self.total_income - self.total_expenses
        print(f'Your total monthly cash flow is: ${self.monthly_cash_flow}')
        self.annual_cash_flow = self.monthly_cash_flow * 12
        print(f'Your annual cash flow is: ${self.annual_cash_flow}')

    # this function collects investment information of the property 
    def get_investment(self):
        self.down_payment = Property.get_input("Please enter any down payment paid: ")
        self.closing_costs = Property.get_input("Please enter any closing costs paid: ")
        self.repair_rehab = Property.get_input("Please enter any repair or rehab costs paid: ")
        self.miscellanous_investment = Property.get_input("Please enter any miscellaneous investments costs paid: ")
        self.total_investment = self.down_payment + self.closing_costs + self.repair_rehab + self.miscellanous_investment
        print(f'Your total investment in the property was: ${self.total_investment}')

    # this calculates and displays the return on investment based on all other information collected
    def calc_roi(self):
        self.roi = self.annual_cash_flow / self.total_investment
        self.roi_percent = str(self.roi * 100) + "%" 
        print(f"Your Return on Investment for {self.name} is: {self.roi_percent}")

    # this function ensures all functions are claled in the correct order and runs the program :)
    def run():
        name = input('Hello friend, what is the name of the property? ')
        print("Great! Please fill in the following prompts with numeric values. At any point you may enter 'quit' to abort and start over")
        property1 = Property(name)
        property1.get_income()
        property1.get_expenses()
        property1.calc_cash_flow()
        property1.get_investment()
        property1.calc_roi()

Property.run()