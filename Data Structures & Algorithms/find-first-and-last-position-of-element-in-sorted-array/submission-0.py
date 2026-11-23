class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        output = []
        start = -1
        l,r = 0,len(nums)-1

        while l<=r:
            mid = int(l+((r-l)/2))

            if nums[mid] == target:
                start = mid
                r = mid-1
            elif nums[mid] < target:
                l = mid+1
            else:
                r = mid-1
        
        
        if start == -1:
            return [-1,-1]

        l,r = start , len(nums)-1
        end = -1
        while l<=r:
            mid = int(l+((r-l)/2))

            if nums[mid] == target:
                end = mid
                l = mid+1
            elif nums[mid] < target:
                l = mid+1
            else:
                r = mid-1
        # print(end)

        return [start,end]