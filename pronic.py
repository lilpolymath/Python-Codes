from math import sqrt

def pronic(a):
    if (a%2 == 0):
         y = int(sqrt(a))
         x = y + 1
         if (a == y *x):
             print("{} is a Pronic Number" .format(a))
             print("The Factors are {} and {}" .format(y, x))
         else:
             print("{} is not a Pronic Number" .format(a))
    else:
        print(" {} is not a pronic number." .format(a))

a = int(input("Enter Number to check : "))
pronic(a)