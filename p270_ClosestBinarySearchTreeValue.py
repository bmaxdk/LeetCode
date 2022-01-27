# 270. Closest Binary Search Tree Value
# https://leetcode.com/problems/closest-binary-search-tree-value/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        stack, res =[root], []
        close = root.val
        while stack:
            node = stack.pop()
            if node:
                if abs(target-node.val) <= abs(target-close): 
                    res.append(node.val)
                    close = node.val
                if node.val < target:
                    stack.append(node.right)
                elif node.val > target:
                    stack.append(node.left)
        return res[-1]
            