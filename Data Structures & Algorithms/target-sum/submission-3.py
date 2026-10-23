class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        mem = {}

        def find(sum,i):
            if i>=len(nums):
                if sum == target:
                    return 1
                return 0

            if (sum,i) in mem:
                return mem[(sum,i)]

            count = find(sum+nums[i],i+1) + find(sum-nums[i],i+1)
            
            mem[(sum,i)] = count
            return count
        
        return find(0, 0)
