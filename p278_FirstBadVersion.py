# 278. First Bad Version
# https://leetcode.com/problems/first-bad-version/
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l,r = 1,n
        while l<r:
            mid = (l+r)//2
            if isBadVersion(mid):
                r = mid
            else:
                l = mid+1
        return l
            