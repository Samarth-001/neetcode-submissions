class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = s.replace(" ", "")
        s = s.lower()
        s = ''.join(c for c in s.lower() if 'a' <= c <= 'z' or  '0'<= c <= '9')
        j = len(s)-1

        if len(s)<2:
            return True

        for i in range(int(j/2)+1):
            if s[i] != s[j-i]:
                return False
        
        return True