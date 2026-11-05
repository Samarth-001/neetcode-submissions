class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        hm = {0:1}
        ans = 0
        sum = 0

        for num in nums:
            sum += num
            
            if sum-k in hm:
                ans+=hm[sum-k]
            
            hm[sum] = hm.get(sum,0)+1
        
        return ans