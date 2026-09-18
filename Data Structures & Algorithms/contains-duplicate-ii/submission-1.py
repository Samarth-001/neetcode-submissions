class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        hm=set()

        for i in range(len(nums)):
            if i>k:
                hm.remove(nums[i-k-1])
            if nums[i] in hm:
                return True
            hm.add(nums[i]) 

        return False