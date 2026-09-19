class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums)-1
        # pivot=0
        while l<r:
            mid = int(l+((r-l)/2))
            if nums[mid]<=nums[r]:
                r = mid
            else:
                l = mid + 1
        
        print(l)

        if target >= nums[0] and target > nums[len(nums)-1]:
            r = l
            l = 0
        else:
            r = len(nums)-1
        
        print(l, r)
        while l<=r:
            mid = int(l+(r-l)/2)
            # print(l, mid, r)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r=mid-1
            else:
                l = mid+1
        
        return -1


        return 0