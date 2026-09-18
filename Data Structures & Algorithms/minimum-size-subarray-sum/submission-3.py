class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        l=0
        r=0
        sum = 0
        ans = len(nums)+1
        length = 0

        while l<=r and r<len(nums) or sum>target:
            # print(nums[l:r], sum, length, ans)
            sum += nums[r]
            length += 1
            r+=1
            while sum >= target:
                # print("inside")
                # print(nums[l:r], sum, length, ans)
                ans = min(ans,length)
                sum-=nums[l]
                l+=1
                length-=1
            if sum>=target:
                # print("i am inside")
                ans = min(ans,length)
        
        # print("FInal answer here:", ans)
        if ans == len(nums)+1:
            return 0
        else:
            return ans
