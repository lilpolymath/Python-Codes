import time
open_bracket, close_bracket = ["(", "{", "[", "<"], [")", "}", "]", ">"]
print(" I'm going to examine if your brackets are closed")
examine = input("Enter any set of characters within any form of brackets: ")
length = len(examine) - 1
position = open_bracket.index(examine[0])
if examine[length] == close_bracket[position]:
    print("\nYes! Your brackets are closed")

else:
    print("\nNope! Your brackets are still open")
time.sleep(5)