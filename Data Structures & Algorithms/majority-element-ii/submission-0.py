class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        hm={}
        ans = []
        for num in nums:
            hm[num] = hm.get(num, 0) + 1
        
        for key, value in sorted(hm.items(), key=lambda x: x[1], reverse=True):
            if value > len(nums)/3:
                ans.append(key)
            else:
                return ans


        return ans