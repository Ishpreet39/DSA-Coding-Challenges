"""Given an array containing N integers and an integer K., Your task is to find the length of the longest Sub-Array with the sum of the elements equal to the given value K.

 

Example 1:
 

Input :
A[] = {10, 5, 2, 7, 1, 9}
K = 15
Output : 4
Explanation:
The sub-array is {5, 2, 7, 1}.
Example 2:

Input : 
A[] = {-1, 2, 3}
K = 6
Output : 0
Explanation: 
There is no such sub-array with sum 6."""

#User function Template for python3

class Solution:
    def lenOfLongSubarr (self, arr, n, k) : 
        #Complete the function
        map = {}
        sum = 0
        len = 0

        for i in range(n):
            sum += arr[i]

            if sum == k:
                len = max(len, i + 1)

            if sum - k in map:
                len = max(len, i - map[sum - k])

            if sum not in map:
                map[sum] = i

        return len
    

