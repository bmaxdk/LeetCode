# 69. Sqrt(x)
# https://leetcode.com/problems/sqrtx/
class Solution:
    def mySqrt(self, x: int) -> int:
        l = 1
        r = x//2
        
        if x <2:
            return x
        while l <=r:
            mid = (l+r)//2
            
            if x == mid*mid:
                return mid
            elif x < mid*mid:
                r = mid -1
            else:
                l = mid+1

        if min(l,r)*min(l,r) > x:
            return min(l,r)-1
        return min(l,r)