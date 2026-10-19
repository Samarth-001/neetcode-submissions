class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        sum = 0
        for num in nums:
            sum += num
        
        if sum%2!=0:
            return False
        
        target = sum/2

        mem = {}
        
        def find(sum,i):
            if i>=len(nums):
                return False

            if sum == target:
                return True
            
            if sum>target:
                return False

            if (sum,i) in mem:
                return mem[(sum,i)]
            
            mem[(sum,i)] = find(sum+nums[i], i+1) or find(sum, i+1)
            return mem[(sum,i)]

        return find(0, 0)