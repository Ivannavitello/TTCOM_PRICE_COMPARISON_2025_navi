# Functions goes here
def not_blank(question):
    """Checks that a user response is not blank"""

    while True:
        # uses 'strip' to remove whitespace before / after
        response = input(question).strip()

        if response != "":
            return response

        print("sorry, this can't be blank. Please try again./n")


def unit(question, valid_answers=('grams', 'kg', 'ml', 'liters'), num_letters=1):
    """Ensures users enter a valid option from a list of valid responses."""
    # this will allow lower case
    valid_answers = [item.lower() for item in valid_answers]
    while True:
        # the strip() method removes any leading, and trailing whitespaces
        # .lower() means that it will accept upper and lower
        response = input(question).strip().lower()
        # match full word or partial letters
        answers = [item for item in valid_answers if response
                   == item or response == item[:num_letters]]
        if answers:
            # if they did not enter a valid answer.
            return answers[0]
        print(f"Invalid input. Please choose from {valid_answers}")

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

print("Hello world")
# loop for testing purposes
while True:

    print()
    item = not_blank("Item: ")
    product_unit = unit("Unit (Grams/Kg/Liters/Ml): ")
    unit_num = num_check("Unit amount:")
    print(f"Your Item is:{item} measured in {unit_num} {product_unit}")



