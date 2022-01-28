# 104. Maximum Depth of Binary Tree
# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Top-Down
# 1. return if root is null
# 2. if root is a leaf node:
# 3.     answer = max(answer, depth)         // update the answer if needed
# 4. maximum_depth(root.left, depth + 1)     // call the function recursively for left child
# 5. maximum_depth(root.right, depth + 1)    // call the function recursively for right child
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
    
# Bottom-Up
# 1. return 0 if root is null                 // return 0 for null node
# 2. left_depth = maximum_depth(root.left)
# 3. right_depth = maximum_depth(root.right)
# 4. return max(left_depth, right_depth) + 1  // return depth of the subtree rooted at root

# Bottom-Up
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        depth_left = self.maxDepth(root.left)
        depth_right = self.maxDepth(root.right)
        return max(depth_left,depth_right)+1