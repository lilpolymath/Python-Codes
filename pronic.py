while True:
    print('Program to check for pronic number')
    n=int(input('Enter the number:'))
    x=(-1+((1+4*n)**(1/2)))/2
    a=int(x)
    if a==x:
        print ('Yes, the number is pronic')
    else: 
        print('Sorry, the number is not pronic')