from random import randint

# The number to guess changes each time it's run
target_num = randint(0, 9)

# Default Values
guess_p1 = 0
guess_p2 = 0
guess_p3 = 0
count = 0
# Default Values for the Guess State
p1isright = False
p2isright = False
p3isright = False

# This Function takes on two arguments to tell us 
# what each player guessed

print("I'm thinking of a number between 0 and 9...")
while True:
    # This is placed here so that the values 
    # can change everytime the loop runs at an instance
    guess_p1 = randint(0, 9)
    guess_p2 = randint(0, 9)
    guess_p3 = randint(0, 9)
    
    #This is placed here so that this values can reflect 
    # if placed outside the loop the list takes on the 
    # default values as members
    guess = [guess_p1, guess_p2, guess_p3]

    print("Number to guess is ", target_num)
    for x in guess:
            print("I'm guessing ", x)
    count += 1

    if guess_p1 == target_num:
        p1isright = True

    if guess_p2 == target_num:
        p2isright = True

    if guess_p3 == target_num:
        p3isright = True

    y = 1
    for x in guess:
        print("Player {0} guessed {1}".format(y, x))
        y = y + 1
    
    # This part runs if at least one of the players gets it right
    if p1isright == True or p2isright == True or p3isright == True:
        print("We have a winner!")
        print("Player one got it right? " + str(p1isright))
        print("Player Two got it right? " + str(p2isright))
        print("Player Three Got it right? " + str(p3isright))
        print("Game Over. After {} rounds." .format(count))
        # This part stops the code from running
        break
    # This re-runs the the code again with all parameters constant
    # except the number to guess
    else:
        print("Players would have to try again")
