class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        seen = set(nums)

        m = 0
        for num in nums:
            m = max(m,num)

        for i in range(1, m):
            if i not in seen:
                return i
        
        return m+1
