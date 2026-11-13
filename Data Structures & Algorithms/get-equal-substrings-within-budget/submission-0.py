class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        prefix = [0]
        psum = 0

        for i in range(len(s)):
            psum += abs(ord(s[i]) - ord(t[i]))
            prefix.append(psum)

        ans = 0
        l = 0

        for r in range(1, len(prefix)):
            while prefix[r] - prefix[l] > maxCost:
                l += 1

            ans = max(ans, r - l)

        return ans