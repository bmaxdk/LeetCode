# 704. Binary Search
# https://leetcode.com/problems/binary-search/
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1

        while l <= r:
            mid = (l+r) //2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                r = mid -1
            else:
                l = mid+1
        return -1


# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         mid = floor(len(nums)/2)
#         left = nums[:mid]
#         right = nums[mid:]
#         if nums[mid] > target:
#             for i in range(len(left)):
#                 if left[i] == target:
#                     return i
#         elif nums[mid] <= target:
#             for i in range(len(right)):
#                 if right[i] == target:
#                     return mid+i
#         return -1
        
