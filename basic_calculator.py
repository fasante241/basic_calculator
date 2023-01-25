# Calculator

#Menu Function
print('''
        Menu Options
        1. Addition
        2. Subtraction
        3. Multiplication
        4. Division
    ''')
options = input('Select from the options above: ')
 
 # Take two numbers 
first_number = float(input('Enter your first number: '))    
second_number = float(input('Enter your second number: '))



class Calculate():
    def __init__(self, first_number, second_number):
        self.first_number = first_number
        self.second_number = second_number
        

    def addition(self):
        self.results = self.first_number + self.second_number 
        print(f'The answer is {self.results}')
    
    def subtraction(self):
        self.results = self.first_number - self.second_number 
        print(f'The answer is {self.results}')

    def multiplication(self):
        self.results = self.first_number * self.second_number 
        print(f'The answer is {self.results}')
    
    def division(self):
        self.results = self.first_number / self.second_number 
        print(f'The answer is {self.results}')
    

# Set Conditions
def conditions(options):

    if options == '1':
        numbers = Calculate(first_number, second_number)
        numbers.addition()

    elif options == '2':
        numbers = Calculate(first_number, second_number)
        numbers.subtraction()

    elif options == '3':
        numbers = Calculate(first_number, second_number)
        numbers.multiplication()

    elif options == '4':
        numbers = Calculate(first_number, second_number)
        numbers.division()


conditions(options)




    
   
    






