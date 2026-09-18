class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        hm = {}
        max_freq = 0
        ans = 0
        l = 0

        for r in range(len(s)):
            
            hm[s[r]] = hm.get(s[r], 0) + 1
            
            max_freq = max(max_freq, hm[s[r]])

            while (r - l + 1) - max_freq > k:
                hm[s[l]] -= 1
                l += 1

            ans = max(ans, r - l + 1)

        return ans