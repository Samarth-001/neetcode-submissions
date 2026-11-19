class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        mnum = max(nums)
        arr = []

        for i in range(len(nums)):
            if nums[i] == mnum:
                arr.append(i)

        if len(arr) < k:
            return 0

        n = len(nums)
        ans = 0

        for i in range(k - 1, len(arr)):
            left_choices = arr[i - k + 1] + 1

            if i + 1 < len(arr):
                right_choices = arr[i + 1] - arr[i]
            else:
                right_choices = n - arr[i]

            ans += left_choices * right_choices

        return ans