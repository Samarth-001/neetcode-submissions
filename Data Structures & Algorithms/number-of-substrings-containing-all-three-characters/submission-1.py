class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        pass

        hm = {
            'a': -1,
            'b': -1,
            'c': -1
        }
        ans = 0
        for i in range(len(s)):
            hm[s[i]] = i

            point = min(hm['a'],hm['b'],hm['c'])
            if point != -1:
                ans += point-0+1
        
        return ans