# 112. Path Sum
# https://leetcode.com/problems/path-sum/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return 0
        stack, res = [(root, targetSum - root.val)], []

        while stack:
            node, num = stack.pop()
            if node:
                res.append((node.val, num))
                if node.right is not None:
                    stack.append((node.right, num - node.right.val))
                if node.left is not None:
                    stack.append((node.left, num - node.left.val))
                if node.left is None and node.right is None and num ==0:
                    return True
        # print(res)
        return False