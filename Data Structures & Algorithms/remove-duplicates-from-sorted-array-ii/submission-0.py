class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        l = 0
        r = 0
        k = 0
        
        while r<len(nums):
            while r<len(nums) and nums[r]==nums[l]:
                r+=1
            r-=1
            print(l,r, k)
            if l == r:
                nums[k] = nums[l]
                k+=1
            else:
                nums[k] = nums[l]
                nums[k+1] = nums[l]
                k+=2
            
            r+=1
            l=r
            
        return k