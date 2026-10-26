class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        currMax = currMin = 0
        maxSum = minSum = nums[0]
        totalSum = 0

        for num in nums:
            currMax = max(num, currMax + num)
            maxSum = max(maxSum, currMax)

            currMin = min(num, currMin + num)
            minSum = min(minSum, currMin)

            totalSum += num

        if maxSum < 0:
            return maxSum

        return max(maxSum, totalSum - minSum)