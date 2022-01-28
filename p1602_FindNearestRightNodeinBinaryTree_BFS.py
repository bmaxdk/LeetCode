# 1602. Find Nearest Right Node in Binary Tree
# https://leetcode.com/problems/find-nearest-right-node-in-binary-tree/
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> Optional[TreeNode]:
        q, req= deque(), []
        
        if root:
            q.append(root)
        while len(q):
            visit = []
            
            for _ in range(len(q)):
                deq = q.popleft()
                if len(visit) !=0 and visit[-1] == u.val:
                    return deq
                visit.append(deq.val)
                
                if deq.left:
                    q.append(deq.left)
                if deq.right:
                    q.append(deq.right)
            req.append(visit)
        else: return None
        return req