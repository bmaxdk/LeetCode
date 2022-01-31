# 70. Climbing Stairs
# https://leetcode.com/problems/climbing-stairs/
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         # a Bottom-up DP implementation:
#         if n == 1:
#             return n
        
#         dp = [0] * (n+1)
#         dp[1] = 1
#         dp[2] = 2
#         for i in range(3, n+1):
#             dp[i] = dp[i-1]+dp[i-2]
#         return dp[n]
        
class Solution:
    def climbStairs(self, n: int) -> int:
        # a top-down DP implementation
        def dp(i):
            if i <= 2:
                return i
            
            if i not in memo:
                memo[i] = dp(i-1) + dp(i-2)
            # store the result inside a hashmap to refer to in the future.
            return memo[i]
            
        memo = {}
        return dp(n)
# With memoization, our time complexity drops to O(n)O(n) - astronomically better, literally.


# class Solution:
#     def climbStairs(self, n: int) -> int:
#     # a top-down (recursive) DP implementation. 
#     # problem! Time Limit Exceeded at testing 44
#         def dp(i):
#             if i <=2:
#                 return i
            
#             return dp(i-1)+dp(i-2)
#         return dp(n)
## without the memoization, this isn't actually dynamic programming - it's just basic recursion. 