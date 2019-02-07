import time as t
import os

valid = [1,2,3]

def find_details(finder):
    file_find = open("../my works/list.txt", "r")
    for line in file_find:
        s = {}
        (s['name'], s['owner'], s['kind'], s['age'], s['vaccinated'], s['comment']) = line.split(",")
        if finder == str(s['name']):
            file_find.close()
            return(s)
        else:
            print("Not Found.")
    file_find.close()

def head():
    print("MENU")
    print('1. Search for Pet')
    print('2. Add Pet Details')
    print('3. Exit')
    check_input()

def search_pet():
    lookup_id = str(input("Enter the Name of the Pet : "))
    details = find_details(lookup_id)
    if details:
        t.sleep(1.5)
        print("\n")
        print("Here is what we have about the Pet {}." .format(details['name']))
        print("1. Pet's Name = " + details['name'])
        print('2. Owner= ' + details['owner'])
        print('3. Kind = ' + details['kind'])
        print('4. Age = ' + details['age'])
        print('5. Vaccinated = ' + details['vaccinated'])
        print('6. General Comments = '+ details['comment'])
        t.sleep(3)
    else:
        time.sleep(3)
        print('Pet not found. Pls Try again.')

#Instructions on hot to add New Pet Details
def instructions():
    print("\n")
    print('NOTE')
    print("1. Pls you can only add a Pet's details at once.")
    print("2. Enter the data using the format below.")
    print("format = Name, Owner, Kind, Age, Vaccinated, Comments")
    print("Example = Gary, Mr. Hopkins, 3 months, Yes, It has been attended to.")
    print("\n")

#Pet Details Function
def add_pet():
    instructions()
    file_read = open('../my works/list.txt', "a")
    data = input('Pet Details : ')
    file_read.write("\n")
    file_read.write(data)
    file_read.close()
    t.sleep(1.5)

def check_input():
    x = int(input("Enter your choice: "))
    if x == 1:
        search_pet()
    elif x == 2:
        add_pet()
    elif x == 3:
        exit()
    elif x not in valid:
        print("Invalid Input")
        x = int(input("Enter your choice: "))

while __name__ == "__main__":        
    head()
    os.system("cls")
