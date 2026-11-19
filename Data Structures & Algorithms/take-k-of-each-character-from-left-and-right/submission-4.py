class Solution:
    def takeCharacters(self, s: str, k: int) -> int:

        if k == 0:
            return 0

        hn = {}

        for ch in s:
            hn[ch] = hn.get(ch, 0) + 1

        for ch in "abc":
            if hn.get(ch, 0) < k:
                return -1
            hn[ch] -= k

        hm = {}
        l = 0
        ans = 0

        for r in range(len(s)):
            hm[s[r]] = hm.get(s[r], 0) + 1

            while any(hm.get(ch, 0) > hn[ch] for ch in "abc"):
                hm[s[l]] -= 1
                l += 1

            ans = max(ans, r - l + 1)

        return len(s) - ans