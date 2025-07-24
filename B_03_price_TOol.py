# Functions goes here
import pandas
from tabulate import tabulate



def not_blank(question):
    """Checks that a user response is not blank"""

    while True:
        # uses 'strip' to remove whitespace before / after
        response = input(question).strip()

        if response != "":
            return response

        print("sorry, this can't be blank. Please try again./n")


def num_check(question, num_type="float", exit_code=None):
    """Checks that response is a float / integer more than zero"""

    if num_type == "float":
        error = "Please enter a number more than 0."
    else:
        error = "Please enter an integer more than 0."

    while True:

        response = input(question)

        # check for exit code return it if entered
        if response == exit_code:
            return response

        # check datatype is correct and that number
        # is more than zero
        try:

            if num_type == "float":
                response = float(response)
            else:
                response = int(response)

            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


def string_check(question, valid_answers=('yes', 'no'),
                 num_letters=1):
    """Checks that users enter the full word
    or the 'n' letter/s of a word  from a list of valid responses"""

    while True:

        response = input(question).lower()

        for item in valid_answers:

            # check if the response is the entire word
            if response == item:
                return item

            # check if it's the first letter
            elif response == item[:num_letters]:
                return item

        print(f"Please choose an option from {valid_answers}")


def make_statement(statement, decoration):
    """Emphasises headings by adding decoration
    at the start and End"""

    return f"{decoration * 3} {statement} {decoration * 6}"

make_statement("Price comparison TOol", decoration="🕷")

def instructions():
    print(make_statement("instructions", "🩻"))

    print(''' 
+++THe User will have to enter the budget in dollars $. 
 After that you will have to list in the items and the weight by grams and kilograms.
 You will then need to enter the cost of that item in dollars $.
The code will then calculate the unit price per KG 
, and it Will recommend the item that is with in the budget.+++''')

def int_check(question):
    """Checks users enter an integer"""

    error = "Please enter an integer."

    while True:

        try:
            # Return the response if it an integer
            response = int(input(question))

            return response

        except ValueError:
            print(error)

def unit(question, valid_answers=('grams', 'kg', 'ml', 'liters'), num_letters=1):
    """Ensures users enter a valid option from a list of valid responses."""
    # this will allow lower case
    valid_answers = [item.lower() for item in valid_answers]
    while True:
        # The strip() method removes any leading, and trailing whitespaces.
        # .lower() means that it will accept upper and lower.
        response = input(question).strip().lower()
        # Match full word or partial letters
        answers = [item for item in valid_answers if response
                            == item or response == item[:num_letters]]
        if answers:
            # if they did not enter a valid answer.
            return answers[0]
        print(f"Invalid input. Please choose from {valid_answers}")
        
def currency(x):
    """Formats numbers as currency ($#.##)"""
    return "${:.2f}".format(x)


def amount_cost():
    """Calculates the Amount cost per item."""
    return float(cost) / float(amount_num)

# Program main heading
print(make_statement("Price comparison tool", "🍿"))
# Ask user if they want  to see the instructions
# display them if necessary
want_instructions = string_check("DO you want to see the instructions")

if want_instructions == "yes":
    instructions()





print("")
# Main Routine goes here __1

    # replace with call to 'not blank' function!
while True:
    budget = int_check("What is your budget?: ")

    # Output error message/ success message
    if budget < 1:
        print(f" Please enter a budget more than $0")
        continue
    elif budget > 9999999999999:
        print(f"Response is too high!")
        continue
    else:
        print(f"your budget is ${budget}")
        break

# Initialize variables
every_item = []
Item_amount = []
# unit_per_grams_ml = []
price_per_item = []
# unit_kg_liters = []
# unit_price_kg_liters = []
amount_price_cost = []
# Data to append
unit_num = 50
cost = 12.50
amount_num = 5
amount_cost = 4
unit_price = 0.00
Converted_amount = 40
converted_unit = 20

# item dictionary
item_dict = {
    'Item': every_item,
    'Item amount': Item_amount,
    # 'Unit per kg/liter': unit_kg_liters,
    # 'Unit of item grams/ml': unit_per_grams_ml,
    '$ Price per item': price_per_item,
    # '$ Unit price per unit': unit_price_kg_liters,
    '$ amount price cost': amount_price_cost

}

# the exit code
EXIT_CODE = "exit"
# this adds a limit and will track the number of items entered
Item_Product = 0
item_limit = 50
Max_items_with_amounts = 20
item_each_item_units = (string_check
                        ("Do you have items that do not have units"
                         " which are measured in amounts (yes or no)? ", valid_answers=("yes", "no"))).lower()
print()
if item_each_item_units == "yes":
    print("Please type in first the Items that do not have units")
    print()

    if item_each_item_units == "yes":
        while True:
            no_unit_items_amount = int_check("How many items that does not have units do you have?")
            if no_unit_items_amount < 2:
                print("Please type in at least 2 to compare the items")
            elif no_unit_items_amount > 20:
                print("Please type in at most 20 to compare the items")
            else:
                break

        for _ in range(no_unit_items_amount):
            product = not_blank("Item :")
            amount_num = num_check("Amount:")
            cost = num_check("Price:$")
            amount_cost = float(cost) / amount_num
            print(f"Your Item is: {product}_{amount_num}")
            print(f"Cost: ${cost}")
            # Needs fix ---
            print(f"Amount per item: {product}: ${amount_cost:.2f}")
            print()
            print()

            every_item.append(product)
            Item_amount.append(amount_num)
            price_per_item.append(cost)
            amount_price_cost.append(amount_cost)


item_lists = pandas.DataFrame(item_dict)
if item_each_item_units == "yes":
    print(tabulate(item_lists[['Item','Item amount','$ Price per item',
                           '$ amount price cost']],
               headers='keys', tablefmt='psql', showindex=False))

unit_less_items_first = item_each_item_units == "yes"
print("Item with units starts here!!!")
print("Exit code is 'exit'")

while Item_Product < item_limit :
    print()
    print()

    # asks the user for The product/ Ask for Item 1
    product = not_blank("Item :")

    if product.lower() == EXIT_CODE:
        break
    elif EXIT_CODE == Item_Product == 0:
        print("Please type at least one item")
        continue
    # Ask Them for the unit for the Product if Grams or Kg
    unit = string_check("Unit (grams/ml or Kg/liters): ", valid_answers=("grams", "kg", "ml", "liters")).lower()
    # Ask the users for the unit amount
    unit_num = num_check("Unit amount:")
    # Users will input the cost for the item in $
    cost = num_check("Price:$")


    # converts the unit
    if unit == "kg":
        converted_unit = "grams"
        Converted_amount = unit_num * 1000
    elif unit == "grams":
        converted_unit = "kg"
        Converted_amount = unit_num / 1000
    if unit == "liters":
        converted_unit = "ml"
        Converted_amount = unit_num * 1000
    elif unit == "ml":
        converted_unit = "liters"
        Converted_amount = unit_num / 1000

    # Prints the item and its unit price in either grams or kg
    if unit == "kg":
        # Prints the converted amount and details
        print(f"Your Item is: {product}_{unit_num}_{unit} "
              f" or {Converted_amount:.2f} {converted_unit}")
        print(f"Cost: ${cost}")
        # Prints the Unit cost per kg
        unit_price = float(cost) / unit_num
        print(f"The unit price of {product} is ${unit_price:.2f} per kg.")

    if unit == "grams":
        print(f"Your Item is: {product}_{unit_num}_{unit} "
              f" or {Converted_amount:.2f} {converted_unit}")
        print(f"Cost: ${cost}")
        # this will  Convert grams to kg and calculate unit price
        unit_price = float(cost) / (unit_num / 1000)
        print(f"The unit price of {product} is ${unit_price:.2f} per kg.")

    if unit == "ml":
        # Prints the converted amount and details
        print(f"Your Item is: {product}_{unit_num}_{unit} "
              f" or {Converted_amount:.2f} {converted_unit}")
        print(f"Cost: ${cost}")
        # Prints the Unit cost per liters
        unit_price = float(cost) / (unit_num/ 1000)
        print(f"The unit price of {product} is ${unit_price:.2f} per liters.")


    if unit == "liters":
        # Prints the converted amount and details
        print(f"Your Item is: {product}_{unit_num}_{unit} "
              f" or {Converted_amount:.2f} {converted_unit}")
        print(f"Cost: ${cost}")
        # Prints the Unit cost per liters
        unit_price = float(cost) / unit_num
        print(f"The unit price of {product} is ${unit_price:.2f} per liters.")

    # Initialize variables

    # Safely append data
    every_item = []
    unit_per_grams_ml = []
    unit_kg_liters = []
    unit_price_kg_liters = []
    price_per_item = []

    item_dict = {
        'Item': every_item,
        'Unit per kg/liter': unit_kg_liters,
        'Unit per grams/ml': unit_per_grams_ml,
        '$ Price per item': price_per_item,
        '$ Unit price per KG/L': unit_price_kg_liters
    }

    every_item.append(product)
    unit_per_grams_ml.append(
        Converted_amount if unit in ["kg", "liters"] else (unit_num if unit in ["grams", "ml"] else ""))
    price_per_item.append(cost)
    # this will convert the unit in kg/l to g/ml
    unit_kg_liters.append(Converted_amount if unit in ["grams", "ml"] else (unit_num if unit in ["kg", "liters"] else ""))
    unit_price_kg_liters.append(unit_price)

# Create Pandas DataFrame from the collected data
item_lists = pandas.DataFrame(item_dict)

# # Display the data as a table
print(tabulate(item_lists[['Item','Unit per kg/liter',
                           'Unit per grams/ml',
                           '$ Price per item','$ Unit price per KG/L'
                        ]], headers='keys', tablefmt='psql', showindex=False))
print(f"Your budget is ${budget}")



