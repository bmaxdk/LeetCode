# 144. Binary Tree Preorder Traversal

# https://leetcode.com/problems/binary-tree-preorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack, output = [root], []
        while stack:
            node = stack.pop()
            
            if node:
                output.append(node.val)
                # #  stack is a LIFO, the right has to go in first to be printed last later when finished printing the left branch
                stack.append(node.right)
                stack.append(node.left)
        return output
        