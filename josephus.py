import math
import time

#x = int(input("Number of people standing : "))
x = 1000
y = math.log(x,2)
z = int(y)
a = x - 2**z
last = 2*a + 1
print("The Last man standing is {}" .format(last))

time.sleep(5)
