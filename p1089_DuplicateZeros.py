# 1089. Duplicate Zeros

#https://leetcode.com/problems/duplicate-zeros/ 

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        
#         zeroes = arr.count(0)
#         n = len(arr)
#         for i in range(n-1, -1, -1):
#             if i + zeroes < n:
#                 arr[i + zeroes] = arr[i]
#             if arr[i] == 0: 
#                 zeroes -= 1
#                 if i + zeroes < n:
#                     arr[i + zeroes] = 0





        size = len(arr)
        for i in range(size-1, -1, -1):
            if arr[i] == 0:
                arr[(i):] =[0] + arr[(i):size-1]
                
        # size = len(arr)
        # for i in range(size):
        #     if arr[size-1-i] == 0:
        #         arr[(size-1-i):] =[0] + arr[(size-1-i):size-1]

