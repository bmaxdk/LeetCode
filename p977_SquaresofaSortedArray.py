# 977. Squares of a Sorted Array

# https://leetcode.com/problems/squares-of-a-sorted-array/
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([num*num for num in nums])


# class Solution:
#     def sortedSquares(self, nums: List[int]) -> List[int]:
#         size = len(nums)
#         result = [0]*size
#         n_left = 0
#         n_right = -1
        
#         for i in range(size):
#             if abs(nums[n_left]) < abs(nums[n_right]):
#                 result[size-1-i] = nums[n_right]**2
#                 n_right -=1
            
#             else:
#                 result[size-1-i] = nums[n_left]**2
#                 n_left +=1
        
#         return result
