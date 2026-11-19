class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maximum = max(nums)
        res = count = l = 0
        for x in nums:
            count += maximum == x
            while count >= k:
                count -= maximum == nums[l]
                l +=1
            res+=l
        return res