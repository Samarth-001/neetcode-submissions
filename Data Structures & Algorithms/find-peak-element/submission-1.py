class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        ans = 0

        l,r = 0,len(nums)-1

        while l<=r:
            mid = l+((r-l)//2)

            if mid == len(nums)-1:
                return mid
                
            if nums[mid]<nums[mid+1]:
                l = mid+1
            else:
                r = mid-1
                ans = mid
        
        return ans