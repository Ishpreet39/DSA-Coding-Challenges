"""Quick Sort is a Divide and Conquer algorithm. It picks an element as a pivot and partitions the given array around the picked pivot.
Given an array arr[], its starting position is low (the index of the array) and its ending position is high(the index of the array).

Note: The low and high are inclusive.

Implement the partition() and quickSort() functions to sort the array.

Example 1:

Input: 
N = 5 
arr[] = { 4, 1, 3, 9, 7}
Output:
1 3 4 7 9
Example 2:

Input: 
N = 9
arr[] = { 2, 1, 6, 10, 4, 1, 3, 9, 7}
Output:
1 1 2 3 4 6 7 9 10"""

class Solution:
    #Function to sort a list using quick sort algorithm.
    def quickSort(self,arr,low,high):
        # code here
        if low<high:
            pivotPos=self.partition(arr,low,high)
            self.quickSort(arr,low,pivotPos-1)
            self.quickSort(arr,pivotPos+1,high)
    
    def partition(self,arr,low,high):
        # code here
        pivot=arr[low]
        i=low
        j=high
        while(i<j):
            while(arr[i]<=pivot and i<=high-1):
                i+=1
            while(arr[j]>pivot and j>=low+1):
                j-=1
            if(i<j):
               arr[i],arr[j]=arr[j],arr[i]
        arr[low],arr[j]=arr[j],arr[low]
        return j
    
