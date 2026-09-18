class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        for i, val in enumerate(nums):
            
            if nums[abs(nums[i])] < 0:
                return abs(val)
            else:
                nums[abs(nums[i])] *= -1
            