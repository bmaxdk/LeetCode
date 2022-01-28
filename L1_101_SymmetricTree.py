# 101. Symmetric Tree
# https://leetcode.com/problems/symmetric-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        return self.dfs(root.left) == self.dfs_right(root.right)

    def dfs(self, root: TreeNode):
        stack, res = [root],[]
        while stack:
            root = stack.pop()
            if root:
                res.append(root.val)
                if root.right is None and root.left is None:
                    continue
                stack.append(root.right)
                stack.append(root.left)
            else:
                res.append(None)
        return res
    
    def dfs_right(self, root: TreeNode):
        stack, res = [root],[]
        while stack:
            root = stack.pop()
            if root:
                res.append(root.val)
                if root.right is None and root.left is None:
                    continue
                stack.append(root.left)
                stack.append(root.right)
            else:
                res.append(None)
        return res