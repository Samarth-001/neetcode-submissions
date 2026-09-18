class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        hm={}

        for i in range(len(nums)):
            if i>k:
                hm.pop(nums[i-k-1])
            if nums[i] in hm:
                return True
            hm[nums[i]] = i

        return False