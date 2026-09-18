class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hm = set()
        l = 0
        ml = 0

        for r in range(len(s)):
            while s[r] in hm:
                hm.remove(s[l])
                l += 1

            hm.add(s[r])
            ml = max(ml, r - l + 1)

        return ml