def make_statement(statement, decoration):
    """Emphasises headings by adding decoration
    at the start and End"""

    return f"{decoration * 3} {statement} {decoration * 6}"


make_statement("Price comparison TOol", decoration="🕷")


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


def instructions():
    print(make_statement("instructions", "🩻"))

    print(''' 
+++THe User will have to enter the budget in dollars $. 
 After that you will have to list in the items and the weight by grams and kilograms.
 You will then need to enter the cost of that item in dollars $.
The code will then calculate the unit price per KG 
, and it Will recommend the item that is with in the budget.+++''')

# Program main heading
print(make_statement("Price comparison tool", "🍿"))
# Ask user if they want  to see the instructions
# display them if necessary
want_instructions = string_check("DO you want to see the instructions")

if want_instructions == "yes":
    instructions()
print()
print()
print("program-continues.>>>>")




