class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        mem = {}

        def find(i,j):
            if i==len(word1):
                return len(word2)-j
            if j==len(word2):
                return len(word1)-i
            
            if (i,j) in mem:
                return mem[(i,j)]

            if word1[i] == word2[j]:
                mem[(i,j)] = find(i+1,j+1)
                return mem[(i,j)]

            mem[(i,j)] = 1 + min(find(i,j+1), find(i+1,j), find(i+1,j+1))
            return mem[(i,j)]

        return find(0,0)