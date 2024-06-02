"""Given a positive integer N, return the Nth row of pascal's triangle.
Pascal's triangle is a triangular array of the binomial coefficients formed by summing up the elements of previous row.
The elements can be large so return it modulo 109 + 7.


Example 1:

Input:
N = 4
Output: 
1 3 3 1
Explanation: 
4th row of pascal's triangle is 1 3 3 1.
Example 2:

Input:
N = 5
Output: 
1 4 6 4 1
Explanation: 
5th row of pascal's triangle is 1 4 6 4 1."""

class Solution:

	def nthRowOfPascalTriangle(self,n):
	    # code here
	    if n == 1:
            return [1]
    
        mod = 10**9 + 7
        ans = [1, 1]
        
        if n == 2:
            return ans
        
        for i in range(3, n + 1):
            temp = [1] * i
            for j in range(1, i - 1):
                temp[j] = (ans[j - 1] + ans[j]) % mod
            ans = temp
        
        return ans
