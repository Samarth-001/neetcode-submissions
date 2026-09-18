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
                    # print("popping", ch)
                    stack.pop()
                else:
                    # print("returning false", ch)
                    return False
            else:
                # print("appending", ch)
                stack.append(ch)
        
        if len(stack) == 0:
            return True
        return False