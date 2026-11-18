class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        pass

        hm = {}
        l,tSum,ans = 0,0,0

        for r in range(len(nums)):
            num = nums[r]

            if (num in hm) and (hm[num]>=k):
                while nums[l]!=num:
                    tSum-=nums[l]
                    hm[nums[l]]-=1
                    l+=1
                tSum-=nums[l]
                hm[nums[l]]-=1
                l+=1
            
            ans = max(ans, (r-l)+1)
            
            tSum+=num
            hm[num] = hm.get(num,0)+1

            # ans = max(ans, tSum)
        
        return (ans)           
