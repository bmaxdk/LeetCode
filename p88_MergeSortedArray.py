# 88. Merge Sorted Array

# https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        while m+n:
            if n == 0:
                break
            if nums1[m-1] > nums2[n-1] and m != 0:
                nums1[m+n-1] = nums1[m-1]
                nums1[m-1] = 0
                m-=1
                
            else:
                nums1[m+n-1] = nums2[n-1]
                nums2[n-1] = 0
                n-=1

            
        
        
        
        return nums1