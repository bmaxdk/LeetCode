# 26. Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        size = len(nums)
        print(size)
        curr = 0
        if len(nums)==0:
            return 
        for i in range(1,size):
            if nums[curr] < nums[i] and nums[curr] != nums[i]:
                curr+=1
                nums[curr] = nums[i]
        return curr+1