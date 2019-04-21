# Guess and Check

# Cube root
x = int(input('Enter an integer:'))
ans = 0

while ans**3 < x:
    ans = ans + 1

if ans ** 3 != x:
    print(str(x) + ' is not a perfect cube')
else:
    print('Cube root of ' + str(x) + ' is ' + str(ans))
# obs: only works for positive integers
    
# Cube root
x = int(input('Enter an integer:'))
ans = 0

# check the cube root of absolute value of x
while ans**3 < abs(x):
    ans = ans + 1

if ans ** 3 != x:
    print(str(x) + ' is not a perfect cube')
else:
    if x < 0:
        # verify and swap the signal
        ans = -ans
    print('Cube root of ' + str(x) + ' is ' + str(ans))


# Cube root most cleaner algorithm    
cube = 8

for guess in range(abs(cube) + 1):
    if guess ** 3 == cube:
        break
    
if guess**3 != abs(cube):
    print(cube, 'is not a perfect cube')
else:
    if cube < 0:
        guess = -guess
    print('Cube root of ' + str(cube) + ' is ' + str(guess))


