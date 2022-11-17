""""
****************************************************************************************
*                Simple Program to generate secure, memorable passwords                *
****************************************************************************************
"""

import random
import string


# List of adjectives for the password
adjectives = ['sleepy', 'slow', 'scary', 'smelly', 'wet', 'fat', 'red', 'orange', 'yellow', 'green',
              'blue', 'purple', 'fluffy', 'white', 'proud', 'brave']

# List of nouns for the password
nouns = ['apple', 'dinosaur', 'ball', 'toaster', 'goat', 'dragon', 'hammer', 'duck', 'panda', 'python',
         'elephant', 'youtube', 'telephone', 'patato']


print("Welcome to Password Picker!")

while True:
    # To pick a random word from a list, we can use the choice() function from the random module
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)

    # To select a random number from 0 to 99, we can use the randrange() function from the random module
    number = random.randrange(0, 100)
    
    special_char = random.choice(string.punctuation)

    # Now let's create the password!!!
    password = adjective + noun + str(number) + special_char
    print(f'\nPassword Suggestion: {password}')

    response = input('Would you like another password? Type Y or N: ').lower()
    if response == 'n':
        break
