"""You are given a positive integer N, return the sum of all prime numbers between 1 and N(inclusive).
 

Example 1:

Input: N = 5
Output: 10
Explanation: 2, 3, and 5 are prime
numbers between 1 and 5(inclusive), and their sum is 2 + 3 + 5 = 10.
Example 2:

Input: N = 10
Output: 17
Explanation: 2, 3, 5 and 7 are prime
numbers between 1 and 10(inclusive), and their sum is 2 + 3 + 5 + 7 = 17."""

#User function Template for python3

class Solution:
    def prime_Sum(self, n):
        # Code here
        lst = []
        isPrime = [True]*(n+1)
        i = 2
        while i*i <= n:
            if isPrime[i]:
                for j in range(i*i, n+1, i):
                    isPrime[j] = False
            i+=1
        for i in range(2,n+1):
            if isPrime[i]:
                lst.append(i)
        return sum(lst)
