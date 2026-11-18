class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        ans = []
        run = 1

        for r in range(len(nums)):

            if r > 0:
                if nums[r] - nums[r - 1] == 1:
                    run += 1
                else:
                    run = 1

            if r >= k - 1:
                if run >= k:
                    ans.append(nums[r])
                else:
                    ans.append(-1)

        return ans