"""Create the multiplication table of a given number N and return the table as an array.


Example 1:

Input:
N = 9

Output:
9 18 27 36 45 54 63 72 81 90

Explanation:
The table of 9 is the output whose 1st 
term is 9 and the 10th term is 90."""

class Solution:
    def getTable(self,N):
        # code here
        table = []
        for i in range(1, 11):  # Multiplying from 1 to 10
            table.append(N * i)
        return table