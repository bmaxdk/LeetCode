# 1295. Find Numbers with Even Number of Digits
#https://leetcode.com/problems/find-numbers-with-even-number-of-digits/


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            if len(str(num)) %2 == 0:
                count +=1
        return count
        
# a= 34
# print(a)
# print(type(a))
# print(str(a))
# print(type(str(a)))
# b = str(34)
# blen= len(b)
# print(blen)
# print(b[-1])