class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        mem = {}
        words = set(wordDict)

        def find(i):
            if i == len(s):
                return True
            
            if i in mem:
                return mem[i]
            
            for word in words:
                if s.startswith(word, i):
                    if find(i+len(word)):
                        mem[i] = True
                        return True
            
            mem[i] = False
            return False

        return find(0)