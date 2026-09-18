class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)

        if n & 1:
            return False

        stack = [None] * n
        top = 0

        for ch in s:
            if ch == '(':
                stack[top] = ')'
                top += 1
            elif ch == '[':
                stack[top] = ']'
                top += 1
            elif ch == '{':
                stack[top] = '}'
                top += 1
            else:
                if top == 0:
                    return False

                top -= 1

                if stack[top] != ch:
                    return False

        return top == 0