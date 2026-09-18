class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def reverse(nums, l, r):
            while l<r:
                nums[l], nums[r] = nums[r], nums[l]
                
                l+=1
                r-=1
        if k>len(nums):
            k %= len(nums)
        l = 0
        r = len(nums) - 1
        reverse(nums, 0, r)
        reverse(nums, l, k-1)
        reverse(nums, k, r)

        


        # [1,2,3,4,5,6,7,8] 2

        # [8,7,6,5,4,3,2,1]

        # [7,8,1,2,3,4,5,6]

        # [5,6,7,8,1,2,3,4]