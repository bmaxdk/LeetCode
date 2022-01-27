# 285. Inorder Successor in BST
# https://leetcode.com/problems/inorder-successor-in-bst/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'Optional[TreeNode]':
        
        if root.val < p.val:
            root = root.right

        stack, res = [root], -9
        while stack:
            node = stack.pop()
            
            if node:
                stack.append(node.right)
                stack.append(node)
                stack.append(node.left)
                
            else:
                if len(stack) ==0:
                    break
                node = stack.pop()
                
                if res == p.val:
                    if node.val > res:
                        return node
                    else:
                        return None
                res = node.val
        return None
