class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        s1 = len(word1)
        s2 = len(word2)

        print(s1)
        print(s2)

        ren = min(s1, s2)
        ans = ""

        for i in range(ren):
            ans = ans + word1[i] + word2[i]
        


        # ren = max(s1,s2) - ren
        print(ren)
        ans = ans + word1[ren: ] + word2[ren: ]

        print(ans)
        return ans