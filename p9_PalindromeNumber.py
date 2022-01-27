# 9. Palindrome Number
# https://leetcode.com/problems/palindrome-number/
class Solution:
    def isPalindrome(self, x: int) -> bool:
        reverse = []
        digit = 1
        x_copy = x
        rev_val = 0
        
        if x <0:
            return False
        
        while x_copy !=0:
            digit*=10
            reverse.append(10*(x_copy%digit)//(digit))
            x_copy -= x_copy%digit
            
        for i in range(len(reverse)):
            rev_val += reverse.pop()*(10**i)
        return x == rev_val
    
# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         if x <0:
#             return False
        
#         reverse = []
#         digit = 1
#         x_copy = x
#         rev_val = 0
#         while x_copy !=0:
#             digit*=10
#             cur_val = x_copy%digit
#             reverse.append(10*cur_val//(digit))
#             x_copy -= cur_val
#         for i in range(len(reverse)):
#             rev_val += reverse.pop()*(10**i)
#         return x == rev_val