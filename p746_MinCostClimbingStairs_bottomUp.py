# 746. Min Cost Climbing Stairs
# https://leetcode.com/problems/min-cost-climbing-stairs/
# botto-up dp
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0]*(len(cost)+1)
        dp[0] = 0
        dp[1] = 0
        for i in range(2, len(cost)+1):
            dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])
        return dp[-1]

# # top-bottom dp
# class Solution:
#     def minCostClimbingStairs(self, cost: List[int]) -> int:
#         def dp(i):
#             if i < 2:
#                 return 0
#             if i not in memo:
#                 memo[i] = min(cost[i-1]+dp(i-1), cost[i-2]+dp(i-2))
#             return memo[i]
#         memo = {}
#         return dp(len(cost))


# class Solution:
#     def minCostClimbingStairs(self, cost: List[int]) -> int:
#         def dp(i):
#             if i == 0:
#                 return 0#cost[0]
#             if i == 1:
#                 return 0#min(cost[1],cost[0])
            
#             if i not in memo:
#                 memo[i] = min(dp(i-1)+cost[i-1], dp(i-2) + cost[i-2])
#             # print(memo[i])
#             return memo[i]
#         memo = {}
        
#         return dp(len(cost))



# Constraints:

# 2 <= cost.length <= 1000
# 0 <= cost[i] <= 999