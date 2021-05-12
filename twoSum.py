class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = dict()
        for i, num in enumerate(nums):
            if num in dic.keys():
                return [dic[num], i]          
            dic[target - num] = i
