class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        hm = {0:-1}
        sum = 0

        for i in range(len(nums)):
            sum += nums[i]
            # print(hm,sum)
            rem = sum%k
            
            if rem in hm:
                if i - hm[rem]>=2:
                    return True
            else:    
                hm[rem] = i
            
        return False