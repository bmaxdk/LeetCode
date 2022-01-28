# 250. Count Univalue Subtrees

# https://leetcode.com/problems/count-univalue-subtrees/submissions/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        self.count = 0
        self.recurse(root, None)
        return self.count
    
    def recurse(self, node, parent): #bottom-up
        #init. condition
        if not node:
            return True
        
        bool_left = self.recurse(node.left, node.val)
        bool_right = self.recurse(node.right, node.val)
        
        if bool_left and bool_right:
            self.count +=1
        bool_parent = bool_left and bool_right and node.val == parent
        return bool_parent
        