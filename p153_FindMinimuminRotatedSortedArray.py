# 153. Find Minimum in Rotated Sorted Array
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums)-1
        if nums[l]<=nums[r]:
            return nums[l]
        while l<r:
            mid = (l+r)//2
            
            if nums[mid]>nums[mid+1]:
                return nums[mid+1]
            
            elif nums[mid]<nums[r]:
                r=mid
            else:
                l=mid