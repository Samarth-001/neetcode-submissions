class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        mem = {}

        def find(i, j):
            
            if i>= len(nums):
                return 0
            
            if (i,j) in mem:
                return mem[(i,j)]

            best = find(i+1, j)
            
            if j==-1 or nums[j]<nums[i]:
                best = max(best, 1+find(i+1, i))
            
            mem[(i,j)] = best
            return best
        
        return find(0,-1)