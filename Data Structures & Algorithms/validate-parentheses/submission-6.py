class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        hm= {
            "}": "{",
            "]": "[",
            ")": "(",
        }
        for ch in s:
            if ch in hm:
                if len(stack) == 0:
                    return False
                if stack[-1] == hm[ch]:

                    stack.pop()
                else:

                    return False
            else:

                stack.append(ch)
        
        return True if not stack else False