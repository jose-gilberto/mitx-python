# Example branching 2

x = int(input('Enter a integer: '))
 
if x % 2 == 0:
    if x % 3 == 0:
        print('Divisible by 3 and 2')
    else:
        print('Divisible by 2 and not by 3')
elif x % 3 == 0:
    print('Divible by 3 and not by 2')
    
print('Done with conditional')
