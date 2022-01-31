# 48. Rotate Image
# https://leetcode.com/problems/rotate-image/
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        #transpose
        for row in range(n):
            for col in range(row+1, n):
                matrix[col][row], matrix[row][col] = matrix[row][col], matrix[col][row]
                
        #reflect
        for row in range(n):
            for col in range(n//2):
                matrix[row][col], matrix[row][-col-1] = matrix[row][-col-1], matrix[row][col]
        # print(matrix)