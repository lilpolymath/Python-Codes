from math import sqrt

def pronic():
    a = int(input("Enter the number to check : "))
    y = int(sqrt(a))
    x = y + 1
    if (a == x*y):
        print("The Numbers are {} and {}" .format(x, y))
    else:
        print("{} is not a Pronic number." .format(a))

pronic()
