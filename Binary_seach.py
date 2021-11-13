'''
Created on Nov 13, 2021

@author: zahra
'''
class Solution:
    def search(self, nums: List[int], target: int, index=0) -> int:
        length = len(nums)
        if length == 0:
            return -1
        if length == 1:
            if nums[0] == target:
                return index
            else:
                return -1
        left = nums[0:length//2]
        right = nums[length//2:length]
        middle = nums[length//2]
        
        if target >= middle:
            return self.search(right, target, length//2 + index)
        else:
            return self.search(left, target, index)
