"""
This program calculates prices for custom house signs.
"""

# Declare and initialize variables here.
# Charge for this sign is $35.00 minimum
# Number of characters: First 5 characters - no additional charge; Each character over 5 - $4.00
# Color of characters: Black/White - no additional cost; Gold Leaf: additional $15.00.
# Type of wood: Pine - no addtional cost; Oak - additional $20.00

def checkInput(numCharsString, woodTypeString, colorString):
    # Decision Structures
    
    # Check if numCharsString is numeric and positive
    if not numCharsString.isdigit():
        return 'Invalid number of characters entered. Please enter a positive number.'
    
    numChars = int(numCharsString)
    if numChars < 0:
        return 'Invalid number of characters entered. Please enter a positive number.'    
    
    # Check if woodTypeString is numeric and either 1 or 2
    if not woodTypeString.isdigit():
        return 'Invalid value entered for wood type. Please enter 1 for Oak or 2 for Pine.'
    
    woodType = int(woodTypeString)
    if woodType not in [1, 2]:
        return 'Invalid value entered for wood type. Please enter 1 for Oak or 2 for Pine.'
    
    # Check if colorString is numeric and either 1 or 2
    if not colorString.isdigit():
        return 'Invalid value entered for character color. Please enter 1 for Gold or 2 for Black/White.'
    
    color = int(colorString)
    if color not in [1, 2]:
        return 'Invalid value entered for character color. Please enter 1 for Gold or 2 for Black/White.'
    
    # If all inputs are valid, return 'valid'
    return 'valid'

# User Input
numCharsString = input("Enter the number of requested characters: ")
woodTypeString = input("Enter 1 or 2 to choose wood type - (1) Oak; (2) Pine: ")
colorString = input("Enter 1 or 2 to choose character color - (1) Gold; (2) Black or White: ")

# Validate user input using checkInput()
validation_result = checkInput(numCharsString, woodTypeString, colorString)

# Write assignment and if statements here as appropriate.

# If validation fails, stop the program and print an error message
if validation_result != 'valid':
    print(validation_result)
else:
    # Charge for this sign.
    charge = 35.00

    # Number of characters.
    numChars = int(numCharsString)

    # Color of characters.
    color = int(colorString)

    # Type of wood.
    woodType = int(woodTypeString)

    # Write assignment and if statements here as appropriate.
    # Calculation for number of characters
    if numChars > 5:
        charge += (numChars - 5) * 4.00

    # Calculation for gold characters
    if color == 1:
        charge += 15.00

    # Calculation for oak wood
    if woodType == 1:
        charge += 20.00
    
    # Output Charge for this sign.
    print("The charge for this sign is $" + str(charge))

