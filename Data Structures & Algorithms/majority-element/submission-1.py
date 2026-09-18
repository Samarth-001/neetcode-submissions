class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        hm = {}
        max = nums[0]

        for num in nums:
            hm[num] = hm.get(num,0) + 1

            if hm[num] > hm[max]:
                max = num
            
            if hm[num] > len(nums)/2:
                return max
        
        return max
