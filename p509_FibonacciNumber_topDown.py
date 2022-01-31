# 509. Fibonacci Number
# https://leetcode.com/problems/fibonacci-number/
class Solution:
    def fib(self, n: int) -> int:
        def dp(i):
            if i <=1:
                return i
            if i not in memo:
                memo[i] = dp(i-1) + dp(i-2)
            return memo[i]
        memo = {}
        return dp(n)

# recursive
# class Solution:
#     def fib(self, n: int) -> int:
#         if n == 0:
#             return 0
#         elif n == 1:
#             return 1
#         else:
#             return self.fib(n-1) + self.fib(n-2)