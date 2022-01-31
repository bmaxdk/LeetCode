# 1137. N-th Tribonacci Number
# https://leetcode.com/problems/n-th-tribonacci-number/
# class Solution:
#     def tribonacci(self, n: int) -> int:
#         if n == 0:
#             return 0
#         elif n <2:
#             return 1
#         dp = [0]*(n+1)
#         dp[0] = 0
#         dp[1] = 1
#         dp[2] = 1
#         for i in range(3, n+1):
#             dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
#         return dp[n]

#top-down dp
class Solution:
    def tribonacci(self, n: int) -> int:
        def dp(i):
            if i == 0:
                return i
            elif i <=2:
                return 1
            if i not in memo:
                memo[i] = dp(i-3)+dp(i-2)+dp(i-1)
            return memo[i]
        memo = {}
        return dp(n)