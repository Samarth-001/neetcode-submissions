class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hm = {}

        l = 0
        r = 0
        ans = 0

        while r < len(s):

            while s[r] in hm:
                hm.pop(s[l])
                l += 1

            hm[s[r]] = 1

            ans = max(ans, r - l + 1)

            r += 1

        return ans