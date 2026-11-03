class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        s = s.strip(" ")
        ans = s.split(" ")

        return len(ans[-1])