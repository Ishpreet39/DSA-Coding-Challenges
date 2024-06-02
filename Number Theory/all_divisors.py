"""Given an integer N, print all the divisors of N in the ascending order.
 

Example 1:

Input : 20
Output: 1 2 4 5 10 20
Explanation: 20 is completely 
divisible by 1, 2, 4, 5, 10 and 20.

Example 2:

Input: 21191
Output: 1 21191
Explanation: As 21191 is a prime number,
it has only 2 factors(1 and the number itself)."""

class Solution:
    def print_divisors(self, N):
        # code here
        divisors = []
        for i in range(1, N + 1):
            if N % i == 0:
                divisors.append(i)
        return divisors