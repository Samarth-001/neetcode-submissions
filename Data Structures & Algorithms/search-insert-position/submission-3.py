class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        l = 0
        r= len(nums)-1
        mid = 0

        while l<=r:
            mid = int(l + ((r-l)/2))
            print(mid)

            if nums[mid] == target:
                return mid
            elif target> nums[mid]:
                l = mid+1
            else:
                r = mid-1
        
        if target> nums[mid]:
            return mid+1
        else:
            return mid