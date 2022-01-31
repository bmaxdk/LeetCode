# 198. House Robber
# https://leetcode.com/problems/house-robber/
# bottom-up
# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         if len(nums) == 1:
#             return nums[0]
        
#         dp = [0]*len(nums)
#         dp[0] = nums[0]
#         dp[1] = max(nums[0], nums[1])
        
#         for i in range(2, len(nums)):
#             dp[i] = max(dp[i-1], dp[i-2]+nums[i])
#         return dp[-1]
        
        
# top-Down
class Solution:
    def rob(self, nums: List[int]) -> int:
        def dp(i):
            #base
            if i == 0:
                return nums[0]
            elif i == 1:
                return max(nums[1],nums[0])
            
            if i not in memo:
                memo[i] = max(dp(i-1), dp(i-2)+nums[i])
            return memo[i]
        memo = {}
        return dp(len(nums)-1)