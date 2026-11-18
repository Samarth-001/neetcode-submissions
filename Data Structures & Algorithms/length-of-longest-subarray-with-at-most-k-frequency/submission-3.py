class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq = {}
        numGreater = 0
        l = 0
        for num in nums:
            if num not in freq:
                freq[num] = 0
            freq[num] += 1
            if freq[num] == k+1:
                numGreater += 1
            if numGreater != 0:
                freq[nums[l]] -= 1
                if freq[nums[l]] == k:
                    numGreater -= 1
                l += 1
        return len(nums) - l