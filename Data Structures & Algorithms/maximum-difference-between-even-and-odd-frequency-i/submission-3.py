class Solution:
    def maxDifference(self, s: str) -> int:
        
        hm = {}

        for ch in s:
            hm[ch] = hm.get(ch,0)+1
        
        eValue = float('inf')
        oValue = 0

        for val in hm.values():
            if val % 2 == 0:
                eValue = min(eValue, val)
            else:
                oValue = max(oValue, val)
        
        return oValue - eValue