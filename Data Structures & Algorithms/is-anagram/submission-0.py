class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s= s.lower()
        t= t.lower()

        hm_s = {}
        hm_t = {}
        
        if (len(s) != len(t)):
            return False
        
        for char in s:
            if char in hm_s:
                hm_s[char] = hm_s[char] + 1
            else:
                hm_s[char] = 1
        for char in t:
            if char in hm_t:
                hm_t[char] = hm_t[char] + 1
            else:
                hm_t[char] = 1
        
        return hm_s == hm_t