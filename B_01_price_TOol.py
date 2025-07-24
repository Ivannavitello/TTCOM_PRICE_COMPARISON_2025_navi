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



# Main Routine goes here __1
# list for panda
# Initialize variables
every_item = []
Item_amount = []
unit_per_grams_ml = []
price_per_item = []
unit_kg_liters = []

# Data to append
unit_num = 50
cost = 12.50
amount_num = 5


# item dictionary
item_dict = {
    'Item': every_item,
    'Item amount': Item_amount,
    'Unit per kg/liter': unit_kg_liters,
    'Unit of item grams/ml': unit_per_grams_ml,
    'Price per item': price_per_item,
}
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
    needs_unit = string_check("Does this item have a unit (yes or no)? ", valid_answers=("yes", "no"))

    if needs_unit == "yes":
        # Ask Them for the unit for the Product if Grams or Kg
        unit = string_check("Unit (grams/ml or Kg/liters): ", valid_answers=("grams", "kg", "ml", "liters"))
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
            unit_price = float(cost) / (unit_num / 1000)  # this will  Convert grams to kg and calculate unit price
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
        print(f"Amount per item {product}: ${amount_cost:.2f}")
    # Safely append data
    every_item.append(product)
    unit_per_grams_ml.append(
        Converted_amount if unit in ["kg", "liters"] else (unit_num if unit in ["grams", "ml"] else ""))
    price_per_item.append(cost)
    Item_amount.append(amount_num if needs_unit == "no" else "")
    unit_kg_liters.append(Converted_amount if unit in ["grams", "ml"] else (unit_num if unit in ["kg", "liters"] else ""))
item_lists = pandas.DataFrame(item_dict)
# # Display the data as a table
print(tabulate(item_lists[['Item','Item amount','Unit per kg/liter',
                           'Unit of item grams/ml',
                           'Price per item',
                        ]], headers='keys', tablefmt='psql', showindex=False))
