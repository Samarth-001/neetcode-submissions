class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        ans = strs[0]
        for obj in strs:
            prefix = ""
            if obj == prefix:
                return prefix
            ren = min(len(obj), len(ans))
            for i in range(ren):
                if obj[i] != ans[i]:
                    
                    ans = prefix
                    break
                prefix += obj[i]
            ans = prefix
        
        return ans