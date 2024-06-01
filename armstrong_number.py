"""For a given 3-digit number n, find whether it is an Armstrong number. 

An Armstrong number of three digits is a number such that the sum of the cubes of its digits is equal to the number itself. Return "Yes" if it is an Armstrong number else return "No".
NOTE: 371 is an Armstrong number since 33 + 73 + 13 = 371

Example 1:

Input: 
n = 153
Output: 
Yes
Explanation: 
153 is an Armstrong number since 13 + 53 + 33 = 153. Hence answer is "Yes".
Example 2:

Input: 
n = 372
Output: 
No
Explanation: 
372 is not an Armstrong number since 33 + 73 + 23 = 378. Hence answer is "No"."""

class Solution:
    def armstrongNumber (self, n):
        # code here 
        def sum_of_cubes(number):
            total = 0
            while number > 0:
                digit = number % 10 #extract the last digit
                total += digit ** 3
                number //= 10   #removes the last digit
            return total
        
        # Check if N is an Armstrong number
        if n == sum_of_cubes(n):
            return "Yes"
        else:
            return "No"