sums = []

def powerSet(items):
    N = len(items) 
    for i in range(2**N): 
        comb=[] 
        for j in range(N): 
            if (i >> j) % 2 == 1:
                comb.append(items[j]) 
        yield comb 

def printSet(sets):
    for x in powerSet(sets):
        print(x)
        sums.append(x)
 
sets = input("Enter the set : ")
sets = eval(sets)

printSet(sets)
print(sums)