def int_check(question):
    """Checks users enter an integer"""

    error = "Please enter an integer."

    while True:

        try:
            # Return the response if it" an integer
            response = int(input(question))

            return response

        except ValueError:
            print(error)


# Main Routine goes here

# loop for testing purposes....
while True:

    print()


    # replace with call to 'not blank' function!
    budget = int_check("What is your budget?: ")
    # Output error message/ success message
    if budget < 1:
        print(f" Please enter a budget more than $0")
        continue
     # doesn't allow high values
    elif budget > 999999999:
        print(f"Response is too high!")
        continue
    # else:
    #     print(f"your budget is ${budget}")
    #     break

print("")
print("Program continues!")