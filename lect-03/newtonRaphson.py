
epsilon = 0.000001

y = 81

guess = y / 2.0
numGuesses = 0

while abs(guess**2 - y) >= epsilon:
    numGuesses += 1
    guess -= (((guess**2) - y) / (2*guess))
    
print('\n\n num of guesses: ' + str(numGuesses) + '\n\n')
print('Square root of ' + str(y) + ' is about ' + str(guess))


