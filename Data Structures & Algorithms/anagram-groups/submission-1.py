class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hm = {}

        for strin in strs:
            smap = [0] * 26
            strin = strin.lower()
            for ch in strin:
                num = ord(ch) - ord('a')
                smap[num] = smap[num] + 1
            
            smap = tuple(smap)
            
            if smap not in hm:
                hm[smap] = [strin]
            else:
                hm[smap].append(strin)
        
        return list(hm.values())