class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        i = n = n_curr = 0
        for ind, char in enumerate(s):
            if char in dic and dic[char] >= i:
                i = dic[char] + 1
                n = max(n, n_curr)
                n_curr = ind - i
            dic[char] = ind
            n_curr += 1
        return max(n, n_curr)