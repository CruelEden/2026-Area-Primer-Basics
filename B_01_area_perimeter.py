# Ask user for width and loop they
# enter a number that is more than zero
def num_check(question):

    error = "please enter number that is more then zero\n"
    while True:

        try:
            # ask the user for a number
            response = float(input(question))

            # check that the number is more than zero
            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)

# Main Routine Starts Here

keep_going = ""
while keep_going == "":

    # get width and height
    width = num_check("Width: ")
    height = num_check("Height: ")

    # Calculate area / perimeter
    area = width * height
    perimeter = 2 * (width + height)

    # Display output
    print()
    print(f"Perimeter: {perimeter} units")
    print(f"Area: {area} square units")

    # Ask if they want to keep going
    keep_going = input("Press enter to keep going or any keys to quit. ")
    print()

print("Thanks for using the area / perimeter calculator")
