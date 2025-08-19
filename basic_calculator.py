import sys


# Calculator

def calculator(first_number, second_number):

# show the list of options
    print('''Choose from the options below: 
      1. Addition
      2. Subtraction
      3. Multiplication
      4. Division''')

    select = input("Select from the options above: ")

    formula = {
        "1" : first_number + second_number,
        "2" : first_number - second_number,
        "3" : first_number * second_number,
        "4" : first_number / second_number,
        }

    results = formula.get(select, "Invalid Input")
    print(round(results, 2))


if __name__ == "__main__":
    print(sys.argv[0])
    first_number = float(input("Enter your first number:"))
    second_number = float(input("Enter your second number:"))
    calculator(first_number, second_number)

   
    






