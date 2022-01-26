# 27. Remove Element
# https://leetcode.com/problems/remove-element/

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        size = len(nums)
        move = 0
        for i in range(size):
            if nums[i-move] == val:
                # nums[i-move] = nums[i-move+1]
                nums.pop(i-move)
                move+=1
            # else:
                # nums[i-move] = nums[i-move]
        new_size = size - move
        return size -move

