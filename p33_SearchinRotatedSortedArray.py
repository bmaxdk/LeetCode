# 33. Search in Rotated Sorted Array
# https://leetcode.com/problems/search-in-rotated-sorted-array/
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l<= r:
            mid = (l+r)//2
            if target == nums[mid]:
                return mid
            
            if nums[l] < nums[r]:
                if nums[mid]<target:
                    l = mid+1
                else:
                    r = mid-1
                    
            else:
                if nums[l] <= nums[mid]:
                    if nums[l] <= target and target < nums[mid]:
                        r = mid-1
                    else:
                        l = mid+1
                else:
                    if nums[mid] < target and target <= nums[r]:
                        l = mid+1
                    else:
                        r = mid-1

        return -1
    
    
    
    