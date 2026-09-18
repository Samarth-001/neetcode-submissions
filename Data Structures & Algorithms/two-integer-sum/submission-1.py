class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hm = {}

        for i, num in enumerate(nums):
            comp = target - num
            if comp in hm:
                return [hm[comp], i]
            hm[num] = i
        
        return []
