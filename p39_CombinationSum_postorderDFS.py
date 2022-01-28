#not Done
# 39. Combination Sum
# https://leetcode.com/problems/combination-sum/

    
# #duplicate:
# class Solution:
#     def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
#         stack, res = [[]], []
#         for i in candidates[::-1]:
#             stack.append([i])
#         while stack:
#             node = stack.pop()
#             # first condition to build level

#             if sum(node)<=target:
#                 if sum(node) == target:
#                     res.append(node)
#                     continue
                    
#                 if len(node) == 1:
#                     for i in candidates[::-1]:
#                         stack.append(node+[i])
#                         if node[0] == i:
#                             break
#                 else:
#                     if len(node) >1:
#                         stack.append(node+[node[-1]])

#         return res
             
# class Solution:
#     def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
#         stack, res = [[]], []
#         for i in candidates[::-1]:
#             stack.append([i])
#         while stack:
#             node = stack.pop()
#             # first condition to build level

#             if sum(node)<=target:
#                 if sum(node) == target:
#                     res.append(node)
#                     continue
                    
#                 if len(node) == 1:
#                     for i in candidates[::-1]:
#                         stack.append(node+[i])
#                         if node[0] == i:
#                             break
#                 else:
#                     if len(node) >1:
#                         stack.append(node+[node[-1]])

#         return res
                    
                
            
    
# class Solution:
#     def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
#         # l = candiates
#         # stack, res = list(zip(l[::-1],[False]*len(l))), []
#         if len(candidates) == 1:
#             if candidates[0] == target:
#                 return[candidates[0]]
#             return[]
#         rev = candidates[::-1]
#         stack, res = [([], False)], []
#         while len(stack):
#             node, visit = stack.pop()
#             # print(len(node))
#         # if node:
#             if visit:
#                 if sum(node) == target:
#                     res.append(node)
#             else:
#                 # if len(l) < len(node):
#                 stack.append((node, True))
#                 if len(node)+1 >len(candidates):
#                     continue
#                 if len(node) == len(candidates)-1:
#                     if sum(node+[node[-1]]) != target:
#                         stack.append((node+[node[-1]],False))
#                 else:
#                     for c in rev:
#                         if sum(node+[c]) <= target:
#                             stack.append((node+[c], False)) #for loop -1
#                     if len(node) >= 1:
#                         if len(rev) == 0:
#                             continue
#                         rev.pop()
#         return res
                    
                
            
    
# #duplicate:
# class Solution:
#     def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
#         # l = candiates
#         # stack, res = list(zip(l[::-1],[False]*len(l))), []
#         stack, res = [([], False)], []
#         while len(stack):
#             node, visit = stack.pop()
#             # print(len(node))
#         # if node:
#             if visit:
#                 if sum(node) == target:
#                     res.append(node)
#             else:
#                 # if len(l) < len(node):
#                 stack.append((node, True))
#                 for c in candidates[::-1]:
#                     if sum(node+[c]) <= target:
#                         stack.append((node+[c], False)) #for loop -1
#         return res
                    
                
            
# class Solution:
#     def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
#         # l = candiates
#         # stack, res = list(zip(l[::-1],[False]*len(l))), []
#         stack, res = [([], False)], []
#         rev = candidates[::-1]
#         i = 0
#         while len(stack):
#             node, visit = stack.pop()
#             # print(len(node))
#         # if node:
#             if visit:
#                 if sum(node) == target:
#                     res.append(node)
#             else:
#                 # if len(l) < len(node):
#                 stack.append((node, True))
#                 if len(node) == 0:
#                     for c in candidates[::-1]:
#                         if sum(node+[c]) <= target:
#                             stack.append((node+[c], False)) #for loop -1
#                 else:
#                     if sum(node) > target or len(node) > len(candidates):
#                         i+=1
#                         continue
#                     # print(node+node[0])
#                     stack.append((node+[rev[i%3]], False))
#                     i+=1
#         return res

    
    