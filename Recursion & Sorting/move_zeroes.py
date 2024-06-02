"""Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 """

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count=0
        for i in nums:
            if i==0:
                count+=1
        pos=0
        for i in nums:
            if i!=0:
                nums[pos]=i
                pos+=1
        for i in range(len(nums)-count,len(nums)):
            nums[i]=0
