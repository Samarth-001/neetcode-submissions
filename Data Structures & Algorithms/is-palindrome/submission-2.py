class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = "".join(char.lower() for char in s if char.isalnum())
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
