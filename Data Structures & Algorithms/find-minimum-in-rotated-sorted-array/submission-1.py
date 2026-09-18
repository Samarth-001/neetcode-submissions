class Solution:
    def findMin(self, nums: List[int]) -> int:

        l = 0
        r = len(nums)-1

        while l<=r:
            if nums[l]<=nums[r]:
                return nums[l]

            mid = int(l+((r-l)/2))
            # print(nums[mid])
            if nums[l]<=nums[mid]:
                l= mid+1
            elif nums[l]>nums[mid]:
                r = mid

