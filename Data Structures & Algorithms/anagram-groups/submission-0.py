class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}

        for word in strs:

            count = [0] * 26

            for char in word:
                index = ord(char) - ord('a')
                count[index] += 1

            key = tuple(count)

            if key not in hm:
                hm[key] = []
            
            hm[key].append(word)
        
        return list(hm.values())