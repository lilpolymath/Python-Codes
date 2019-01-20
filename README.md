# Python-Codes
A repo containing my Python codes. More classifications would be made later.
This would contain solutions to various questions, Algorithms, OOP codes and miscellaneous codes. Time Complexity would be reduced to the barest minimum.
Please note that this is just the beginning don't get disappointed if your hopes are not dashed(smiles)

# Smallest Common Multiple Explanation
* Question
Find the smallest common multiple of the provided parameters that can be evenly divided by both, as well as by all sequential numbers in the range between these parameters.

The range will be an array of two numbers that will not necessarily be in numerical order.

For example, if given 1 and 3, find the smallest common multiple of both 1 and 3 that is also evenly divisible by all numbers between 1 and 3. The answer here would be 6.

* Explanation to Solution

Smallest common multiple is the same thing as LCM. That can be evenly divided means to divide with no remainder. 

An array would be the input but it may not be in numerical order so you have to find the max and min of the range for proper formatting.

LCM of two numbers = the product of those two numbers divided by their GCD.

Luckily for us, LCM operation is associative i.e
LCM (a, b, c) = LCM ( LCM (a, b) , c) or vice versa and you can spread it.

So, we just have to keep iterating through the array to figure the final LCM.

It is normal to think how would that work, but it does all thanks to our GCD that gives us a very small number. 

And my code uses space as delimiter but you'll have to find a way to parse in array.
For frequent updates make sure you watch and star thie repo. Thanks.
