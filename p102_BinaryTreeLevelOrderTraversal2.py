# 102. Binary Tree Level Order Traversal
# https://leetcode.com/problems/binary-tree-level-order-traversal/

from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        q, req= deque(), []
        
        if root:
            q.append(root)
        while len(q):
            visit = []
            
            for _ in range(len(q)):
                deq = q.popleft()
                visit.append(deq.val)
                
                if deq.left:
                    q.append(deq.left)
                if deq.right:
                    q.append(deq.right)
            
            req.append(visit)
        return req