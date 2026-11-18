class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        pass

        prefSum = 0
        hm={0:1}

        ans = 0

        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                prefSum += 1
            
            if prefSum-k in hm:
                ans+=hm[prefSum-k]
            
            hm[prefSum] = hm.get(prefSum,0)+1

        return ans