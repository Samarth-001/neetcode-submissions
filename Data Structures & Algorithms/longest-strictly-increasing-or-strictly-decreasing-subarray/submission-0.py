class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1


        ans = 1
        iCount = 1
        dCount = 1

        for i in range(len(nums)-1):
            if nums[i]<nums[i+1]:
                iCount+=1
                dCount = 1
            elif nums[i]>nums[i+1]:
                dCount += 1
                iCount = 1
            else:
                dCount = 1
                iCount = 1
            ans = max(ans, max(iCount,dCount))
            print(i, iCount, dCount)
        
        return ans