"""For a given number N check if it is prime or not. A prime number is a number which is only divisible by 1 and itself.
 

Example 1:

Input:
N = 5
Output:
1
Explanation:
5 has 2 factors 1 and 5 only."""
class Solution:
    def isPrime(self, n):
        import math
        if n <= 1:
            return 0
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return 0
        return 1
