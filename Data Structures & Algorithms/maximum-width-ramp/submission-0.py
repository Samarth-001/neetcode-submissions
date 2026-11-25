class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        pass

        st = []

        for i in range(len(nums)):
            if not st or nums[st[-1]]>nums[i]:
                st.append(i)
        
        # print(st)

        ans = 0

        for i in range(len(nums)-1,-1,-1):
            # print(i)
            if not st:
                break

            if nums[i]<nums[st[-1]]:
                continue
            
            while st and nums[i]>=nums[st[-1]]:
                ans = max(ans, i-st[-1])
                st.pop()
        
        return ans