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

# After that the code will ask the users for the cost of the item

# Program main heading
print(make_statement("Price comparison tool", "🍿"))
# Ask user if they want  to see the instructions
# display them if necessary
print("")


# Main Routine goes here __1


# ask user for their budget
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
unit_per_grams_ml = []
price_per_item = []
unit_kg_liters = []
unit_price_kg_liters = []
amount_price_cost = []
# Data to append
unit_num = 50
cost = 12.50
amount_num = 5
amount_cost = 4
unit_price = 0.00


# item dictionary
item_dict = {
    'Item': every_item,
    'Item amount': Item_amount,
    'Unit per kg/liter': unit_kg_liters,
    'Unit of item grams/ml': unit_per_grams_ml,
    '$ Price per item': price_per_item,
    '$ Unit price per unit': unit_price_kg_liters,
    '$ amount price cost': amount_price_cost
}
print()
# Get item name and check it;s not blank
# the exit code
EXIT_CODE = "exit"
# this adds a limit and will track the number of items entered
Item_Product = 0
item_limit = 50
while Item_Product < item_limit :
    # asks the user for The product/ Ask for Item 1
    product = not_blank("Item :")
    # an exit code that breaks the loop in the item: part
    if product.lower() == EXIT_CODE:
        break
    elif EXIT_CODE == Item_Product == 0:
        print("Please type at least one item")
        continue

    # This checks if the Item the users typed in needs a unit or no.
    print()
    needs_unit = string_check("Does this item have a unit (yes or no)? ", valid_answers=("yes", "no"))

    if needs_unit == "yes":
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


    else:
        # For items like 12 eggs
        amount_num = num_check("Amount:")
        cost = num_check("Price:$")
        amount_cost = float(cost) / amount_num
        print(f"Your Item is: {product}_{amount_num}")
        print(f"Cost: ${cost}")
        # Needs fix ---
        print(f"Amount per item: {product}: ${amount_cost:.2f}")

    # Safely append data
    every_item.append(product)
    # this will convert the unit in g/ml to kg/l
    unit_per_grams_ml.append(
        Converted_amount if unit in ["kg", "liters"] else (unit_num if unit in ["grams", "ml"] else ""))
    price_per_item.append(cost)
    Item_amount.append(amount_num if needs_unit == "no" else "")
    # this will convert the unit in kg/l to g/ml
    unit_kg_liters.append(Converted_amount if unit in ["grams", "ml"] else (unit_num if unit in ["kg", "liters"] else ""
                                                                            if needs_unit == "no" else ""))
    print("needs_unit", needs_unit)
    unit_price_kg_liters.append(unit_price if needs_unit == "yes" else "")
    amount_price_cost.append(amount_cost if needs_unit == "no" else "")
item_lists = pandas.DataFrame(item_dict)

# # Display the data as a table
print(tabulate(item_lists[['Item', 'Item amount', 'Unit per kg/liter',
                           'Unit of item grams/ml',
                           '$ Price per item', '$ Unit price per unit',
                           '$ amount price cost'
                           ]], headers='keys', tablefmt='psql', showindex=False))
print(f"Your budget is ${budget}")


