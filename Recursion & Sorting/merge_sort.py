"""Given an array arr[], its starting position l and its ending position r. Sort the array using merge sort algorithm.
Example 1:

Input:
N = 5
arr[] = {4 1 3 9 7}
Output:
1 3 4 7 9
Example 2:

Input:
N = 10
arr[] = {10 9 8 7 6 5 4 3 2 1}
Output:
1 2 3 4 5 6 7 8 9 10"""

class Solution:
    def merge(self,arr, l, m, r): 
        # code here
        left = l
        
        right = m+1
        temp = []

        while left <= m and right <= r:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                right += 1

        while left <= m:
            temp.append(arr[left])
            left += 1

        while right <= r:
            temp.append(arr[right])
            right += 1

        for i, val in enumerate(temp):
            arr[l + i] = val
        
    def mergeSort(self,arr, l, r):
        #code here
        if l>=r:
            return
        
        mid = (l+r)//2
        self.mergeSort(arr , l , mid)
        self.mergeSort(arr , mid+1 , r)
        self.merge(arr , l , mid , r)

