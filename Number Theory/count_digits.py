"""Given a number N. Count the number of digits in N which evenly divide N.

Note :- Evenly divides means whether N is divisible by a digit i.e. leaves a remainder 0 when divided.
 

Example 1:

Input:
N = 12
Output:
2
Explanation:
1, 2 both divide 12 evenly
Example 2:

Input:
N = 23
Output
0
Explanation:
2 and 3, none of them
divide 23 evenly"""

class Solution:
    def evenlyDivides (self, N):
        # code here
        count = 0
        temp = N
        while temp > 0:
            digit = temp % 10
            if digit != 0 and N % digit == 0:
                count += 1
            temp //= 10
        return count

#temp % 10 extracts the last digit of temp, and temp //= 10 removes the last digit in each iteration