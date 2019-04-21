# Control flow

# While loop
n = input('You are in the lost forest. Go left or right? ')

while n == 'right':
    n = input('You are in the lost forest. Go left or right? ')

print('You got out of the lost forest.')


x = 0

while x < 5:
    print(x)
    x += 1 # increment

# For loop
for x in range(5):
    print(x)
    
# range (<start>,<stop>,<step>)

# Break statement
n = 0

while True:
    n += 1
    if n > 5:
        break
