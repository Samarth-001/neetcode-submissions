class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return nums[0]
        
        mem = {}
        
        def find(i):
            # print(i)
            if i>=n:
                return 0
            
            if i in mem:
                return mem[i]

            mem[i] = nums[i] + max(find(i+2),find(i+3))
            return mem[i]

        return max(find(0), find(1))