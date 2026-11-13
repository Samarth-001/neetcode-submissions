class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x

        if target < 0:
            return -1

        if target == 0:
            return len(nums)

        l = 0
        wSum = 0
        maxLen = -1

        for r in range(len(nums)):
            wSum += nums[r]

            while wSum > target:
                wSum -= nums[l]
                l += 1

            if wSum == target:
                maxLen = max(maxLen, r - l + 1)

        if maxLen == -1:
            return -1

        return len(nums) - maxLen