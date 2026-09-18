class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        hm= {
            "}": "{",
            "]": "[",
            ")": "(",
        }
        for ch in s:
            if ch in ["[","{","("]:
                print("appending", ch)
                stack.append(ch)
            elif ch in ["}","]",")"]:
                if len(stack) == 0:
                    return False
                if stack[-1] == hm[ch]:
                    print("popping", ch)
                    stack.pop()
                else:
                    print("returning false", ch)
                    return False
        
        if len(stack) == 0:
            return True
        return False

        