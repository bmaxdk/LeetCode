# 94. Binary Tree Inorder Traversal

# https://leetcode.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack, visited = [root], []
        
        while stack:
            node = stack.pop()
            if node:
                stack.append(node.right)
                stack.append(node)
                stack.append(node.left)
            if node is None:
                if len(stack) ==0:
                    break
                node = stack.pop()
                visited.append(node.val)
        return visited