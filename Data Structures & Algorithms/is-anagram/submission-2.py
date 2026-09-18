class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        hm1 = {}
        hm2 = {}

        for ch in s:
            if ch not in hm1:
                hm1[ch] = 1
            hm1[ch] = hm1[ch] + 1
        
        for ch in t:
            if ch not in hm2:
                hm2[ch] = 1
            hm2[ch] = hm2[ch] + 1
            
        if hm1==hm2:
            return True
        return False