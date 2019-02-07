BeerNum = 10
word = "bottles"

while BeerNum > 0:
    if BeerNum == 1:
        word = "bottle"
    print("{0} {1} of Beer on the Wall".format(BeerNum, word))
    print("{0} {1} of Beer".format(BeerNum, word))
    print("Take one Down.")
    print("Pass it around.")
    BeerNum = BeerNum - 1
    if BeerNum > 0:
        print("{0} {1} of Beer on the wall".format(BeerNum, word))
    else:
        print("No more Bottles of beer on the wall")