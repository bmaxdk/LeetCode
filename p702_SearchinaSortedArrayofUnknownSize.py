# 702. Search in a Sorted Array of Unknown Size
# https://leetcode.com/problems/search-in-a-sorted-array-of-unknown-size/
# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        r = 1
        while reader.get(r)<target:
            r<<=1 #r*=2(faster)

        l = r>>1 
        while l<=r:
            mid = (l+r)>>1
            if reader.get(mid) == target:
                return mid
            elif reader.get(mid)<target:
                l=mid+1
            else:
                r=mid-1
        
        return -1
            

# class Solution:
#     def search(self, reader, target):
#         """
#         :type reader: ArrayReader
#         :type target: int
#         :rtype: int
#         """
#         check= True
#         condition = True
#         r=0
#         while condition:
#             if reader.get(r)<2147483647:
#                 if reader.get(r)== target:
#                     return r
#                 elif reader.get(r) < target:
#                     r+=2
#                 else:
#                     r-=1
#                     condition=check
#                     check = False
#             else:
#                 condition = check
#                 r-=1
#                 check=False
#         return -1
    
    
    