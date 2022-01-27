# 98. Validate Binary Search Tree
# https://leetcode.com/problems/validate-binary-search-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack, res = [root],[]
        while stack:
            node = stack.pop()
            
            if node:
                stack.append(node.right)
                stack.append(node)
                stack.append(node.left)
                
            else:
                if len(stack)==0:
                    break
                node = stack.pop()
                if len(res)!=0:
                    if res[-1]>=node.val:
                        return False
                res.append(node.val)
                
        return True