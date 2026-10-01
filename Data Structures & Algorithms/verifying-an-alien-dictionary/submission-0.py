class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        if len(words) <= 1:
            return True

        hm = {}
        i = 0
        for ch in order:
            hm[ch] = i
            i+=1
        
        # print(hm)

        for i in range(len(words)-1):
            for j in range(len(words[i])):
                if j>len(words[i+1])-1:
                    return False

                if hm[words[i][j]] < hm[words[i+1][j]]:
                    break
                elif hm[words[i][j]] == hm[words[i+1][j]]:
                    continue
                else:
                    return False

        return True