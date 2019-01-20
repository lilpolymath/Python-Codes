# Little setback is that how input would be given
# Gets input separate by spaces
arr = [int(x) for x in input().split()]

# this part gets the min and max incase 
# not properly formatted from line 3
max = max(arr)
min = min(arr)

# Populating the array
between = []
for i in range(min, max+1):
    between.append(i)

# Finds the LCM
def find_lcm(num1, num2): 
	if(num1>num2): 
		num = num1 
		den = num2 
	else: 
		num = num2 
		den = num1 
	rem = num % den 
	
	# This part handles the GCD
	while(rem != 0): 
		num = den 
		den = rem 
		rem = num % den 
	gcd = den
	
	# This is the formula for getting the LCM from GCD
	lcm = int(int(num1 * num2)/int(gcd)) 
	return lcm 
	
# For the first sets
num1 = between[0] 
num2 = between[1] 
lcm = find_lcm(num1, num2) 

# Iterates through the whole array and compares
# This part works because it uses the GCD and no matter what
for i in range(2, len(between)): 
	lcm = find_lcm(lcm, between[i]) 
	
print(lcm) 
