class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return nums[0]
            
        nums1 = nums[:n-1]
        nums = nums[1:n]
        n-=1
        
        mem = {}
        mem1 = {}
        def findNums(i):
            if i>=n:
                return 0

            if i in mem:
                return mem[i]

            mem[i] = nums[i] + max(findNums(i+2), findNums(i+3))
            return mem[i]


        def findNums1(i):
            if i>=n:
                return 0
            
            if i in mem1:
                return mem1[i]

            mem1[i] = nums1[i] + max(findNums1(i+2), findNums1(i+3))
            return mem1[i]
        
        numsans = max(findNums(0), findNums(1))
        numsans1 = max(findNums1(0), findNums1(1))
        print(numsans, numsans1)
        return max(numsans, numsans1)