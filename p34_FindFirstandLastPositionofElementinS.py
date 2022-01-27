# 34. Find First and Last Position of Element in Sorted Array
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l,r = 0, len(nums)-1
        
        leftBound = self.searchBound(nums,target,True)
        if len(nums) == 0 or nums[leftBound] !=target:
            return [-1,-1]
        rightBound = self.searchBound(nums,target,False)
        
        return [leftBound,rightBound]
        
        
    def searchBound(self, nums:List[int], target: int, isLeftBound: bool) -> int:
        l,r = 0, len(nums)-1
        if isLeftBound:
            while l<r:
                mid=(l+r)//2
                if target<=nums[mid]:
                    r=mid
                else:
                    l=mid+1
            return l
        else:
            while l<=r:
                mid=(l+r)//2
                if nums[mid]<=target:
                    l=mid+1
                else:
                    r=mid-1
            return r
#################################################################
        
#         # find left bound
#         while l<r:
#             mid=(l+r)//2
#             if target<=nums[mid]:
#                 r = mid
#             else:
#                 l =mid+1

#         #find right bound
#         # while l<=r:
#         #     mid=(l+r)//2
#         #     if nums[mid]<=target:
#         #         l = mid+1
#         #     else:
#         #         r = mid-1
#         print(len(nums))
#         print(l, mid, r)