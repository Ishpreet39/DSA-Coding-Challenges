"""You are given an integer n, return the fibonacci series till the nth(0-based indexing) term. Since the terms can become very large return the terms modulo 109+7.

Example 1:

Input:
n = 5
Output:
0 1 1 2 3 5
Explanation:
0 1 1 2 3 5 is the Fibonacci series up to the 5th term.
Example 2:

Input:
n = 10
Output:
0 1 1 2 3 5 8 13 21 34 55
Explanation:
0 1 1 2 3 5 8 13 21 34 55 is the Fibonacci series up to the 10th term."""

class Solution:
    def series(self, n):
        # Code here
        if n == 0:
            return [0]
        if n == 1:
            return [0, 1]
        ans = [0, 1]
        for i in range(2, n+1):
            ans.append((ans[i-1] + ans[i-2]) % (10**9 + 7)) 
        return ans

