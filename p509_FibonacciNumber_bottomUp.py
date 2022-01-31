# 509. Fibonacci Number
# https://leetcode.com/problems/fibonacci-number/

#dp bottom-up implementation
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return n
        dp = [0]*(n+1)
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[n]

# #dp top-Down implementation
# class Solution:
#     def fib(self, n: int) -> int:
#         def dp(i):
#             if i <=1:
#                 return i
#             if i not in memo:
#                 memo[i] = dp(i-1) + dp(i-2)
#             return memo[i]
#         memo = {}
#         return dp(n)

# recursive
# class Solution:
#     def fib(self, n: int) -> int:
#         if n == 0:
#             return 0
#         elif n == 1:
#             return 1
#         else:
#             return self.fib(n-1) + self.fib(n-2)