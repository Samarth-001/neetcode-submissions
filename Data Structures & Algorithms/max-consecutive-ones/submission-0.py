class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        ans = 0
        count = 0

        for num in nums:
            if num == 0:
                count = 0
                continue
            
            count +=1
            ans = max(count,ans)
        
        return ans    
            