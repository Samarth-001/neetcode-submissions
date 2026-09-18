class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        l = 0
        curr_sum = 0
        ans = len(nums) + 1

        for r in range(len(nums)):

            curr_sum += nums[r]

            while curr_sum >= target:
                ans = min(ans, r - l + 1)

                curr_sum -= nums[l]
                l += 1

        return 0 if ans == len(nums) + 1 else ans