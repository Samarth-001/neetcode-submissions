class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s= s.replace(" ","").lower()
        s = ''.join(c.lower() for c in s if c.isalnum())
        l = len(s)
        
        if l == 0:
            return True
        
        i = 0
        l = l-1
        print(s)
        while(i<l):
            if s[i] != s[l]:
                return False
            i = i+1
            l = l-1
        
        return True
