# Number guessing game
# Created: 8/23/24

# Import required libraries
import random
import math

print("You want to play a number guessing game?\nSure, why not. I'll choose the number, and you guess. Just one thing though...\n")
# Run data validation on user input in a loop until inputs are correct
while True:
    # Try getting user to input values for the lower and upper bounds
    try:
        # Ask the user for input
        print("What should the number I choose be between?")
        # Save entered values to their respective variables
        lowerBound, upperBound = input("Type both of them here: ").split()
        
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
            if lowerBound == upperBound:
                # Throw a SyntaxError to be processed and shown to the user if the values are equal
                raise SyntaxError
            elif lowerBound > upperBound:
                # Switch their values if the entered lower bound is larger than the upper bound
                intermediateValue = lowerBound
                lowerBound = upperBound
                upperBound = intermediateValue
                # Throw a IndexError if the entered values were not in ascending order
                raise IndexError
    # Catch the automatic ValueError if two values were not entered
    except ValueError:
        print("I need two numbers to choose a number between. Try again\n")
    # Catch the thrown TypeError if the entered values could not be converted to integers
    except TypeError:
        print("Those aren't both numbers. Try again\n")
    # Catch the thrown SyntaxError if the entered values were equal
    except SyntaxError:
        print("I need the two numbers you choose to be different. Try again\n")
    # Catch the thrown IndexError if the entered values were not in ascending order
    except IndexError:
        print("Looks like you gave me the numbers out of order. No worries! I'll just switch them around\n")
        break
    # Exit the loop if no exceptions were caught
    else:
        print("")
        break


# Select a random number within the entered range
selectedNumber = random.randint(lowerBound, upperBound)
# Remind the user of the guessing range that was selected
print("Alright, I finished choosing a number between " + str(lowerBound) + " and " + str(upperBound) + ". You can guess now!")
# Troubleshooting Code
print("Selected number: " + str(selectedNumber))


# Calculate the most amount of guesses required to determine the selected number
totalPossibilities = upperBound - lowerBound + 1
requiredGuesses = math.ceil(math.log(totalPossibilities,2))
# Display the most amount of guesses required to the user
print("Hint: You can guess the number I thought of in at most " + str(requiredGuesses), end=" ")
# Change the wording used if more than one guess is required
if requiredGuesses > 1:
    print("guesses.", end=" ")
else:
    print("guess.", end=" ")
# Display the losing condition to the user
print("If it takes you more, then you lose\n")


# Initialize the total amount of user guesses
totalGuesses = 0
# Run data validation on user input in a loop until selected number is guessed
while True:
    # Try getting user input on the value they guess
    try:
        # Ask the user for input and save entered value to its respective variable
        userGuess = input("What do you guess?\nType it here: ")
        # Split the input at any whitespace
        intermediateValue = userGuess.split()
        # Determine if more than one input was made
        if len(intermediateValue) > 1:
            # Throw a ValueError if more than one input was made
            raise ValueError
        
        # Try converting the input into an integer
        try:
            userGuess = int(userGuess)
        # Catch the automatic ValueError if entered values cannot be converted to integers
        except ValueError:
            # Throw a TypeError to be processed and shown to the user
            raise TypeError
        # Compare the guessed value if no exceptions were caught
        else:
            # Increase the number of guesses made by 1
            totalGuesses = totalGuesses + 1
            # Compare the guess to the selected number
            if userGuess > selectedNumber:
                # Inform the user their guess was too high
                print("You guessed too high. Try again!\n")
            elif userGuess < selectedNumber:
                # Inform the user their guess was too low
                print("You guessed too low. Try again!\n")
            else:
                # Inform the user their guess was correct
                print("Yup, that's it!", end=" ")
                # Change ending message based on the amount of guesses taken
                if totalGuesses == 1:
                    print("I can't believe it only took you a single guess!\nYou're not a mind reader or something are you?\n")
                elif totalGuesses < requiredGuesses:
                    print("I can't believe it only took you " + str(totalGuesses) + " guesses.\nYou must be super smart!\n")
                elif totalGuesses == requiredGuesses:
                    print("You guessed what number I was thinking of in exactly the amount of tries I said it should\n")
                else:
                    print("Too bad you still lose though.\nIt took you " + str(totalGuesses - requiredGuesses) + " more than what it should've (" + str(requiredGuesses) + ")\n")
                # Exit the loop after the selected number is guessed
                break
    # Catch the thrown ValueError if more than one input was made
    except ValueError:
        print("You can only guess one number at a time. Try again\n")
    # Catch the thrown TypeError if the entered value could not be converted to an integer
    except TypeError:
        print("That's not a number, you have to guess a number. Try again\n")
