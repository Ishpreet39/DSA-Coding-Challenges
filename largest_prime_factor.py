"""Given a number N, the task is to find the largest prime factor of that number.
 Example 1:

Input:
N = 5
Output:
5
Explanation:
5 has 1 prime factor i.e 5 only.
Example 2:

Input:
N = 24
Output:
3
Explanation:
24 has 2 prime factors 2 and 3 in which 3 is greater."""

class Solution:
    def largestPrimeFactor (self, N):
        # code here
        max_prime = -1
        n = N
        while n % 2 == 0:
            max_prime = 2
            n //= 2
        for i in range(3, int(n**0.5) + 1, 2):
            while n % i == 0:
                max_prime = i
                n //= i
        if n > 2:
            
            max_prime = n
        return max_prime