class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        hm = set(nums)
        
        ans = 0
        for num in nums:
            seq = 0
            if num-1 not in hm:
                while num in hm:
                    num +=1
                    seq = seq + 1
                
            ans = max(ans,seq)
        
        return ans
                                    