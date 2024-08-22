# Number guessing game
# Created: 8/20/24

# Import required libraries
import random

# Run data validation on user input in a loop until inputs are correct
while True:
    # Try getting user to input values for the lower and upper bounds
    try:
        # Ask user for input
        print("Enter the lower and upper bounds of your desired range, separated by a space")
        # Save entered values to their respective variables
        lowerBound, upperBound = input("Desired bounds: ").split()
        # Try converting entered values to integers
        try:
            lowerBound = int(lowerBound)
            upperBound = int(upperBound)
        # Catch the automatic ValueError if entered values cannot be converted to integers
        except ValueError:
            # Throw a TypeError to be processed and shown to the user
            raise TypeError
        # Execute this if no ValueError was thrown
        else:
            # Compare the entered lower and upper bound
            if lowerBound >= upperBound:
                # Throw a SyntaxError to be processed and shown to the user if the values are equal and/or not in ascending order
                raise SyntaxError
    # Catch the automatic ValueError if two values were not entered
    except ValueError:
        print("Incorrect number of values entered. Please make sure to enter two values\n")
    # Catch the thrown TypeError if the entered values could not be converted to integers
    except TypeError:
        print("Incorrect data type entered. Please make sure to enter two integer values\n")
    # Catch the thrown SyntaxError if the entered values were equal and/or not in ascending order
    except SyntaxError:
        print("Entered lower bound is greater than or equal to the upper bound. Please make sure to enter two distinct integers values in ascending order\n")
    # Exit the loop if no exceptions were caught
    else:
        print("")
        break

print("Guessing bounds: [" + str(lowerBound) + ", " + str(upperBound) + "]")
selectedNumber = random.randint(lowerBound, upperBound)
print("Selected number: " + str(selectedNumber))
