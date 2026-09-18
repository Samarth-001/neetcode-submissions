class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s)<2:
            return False

        hm={"}":"{", "]":"[", ")":"("}

        stack = []

        for ch in s:
            if ch in ["{", "(", "["]:
                stack.append(ch)
            else:
                # print(hm[ch], stack[-1])
                if not stack:
                    return False
                if hm[ch]!=stack[-1]:
                    return False
                stack.pop()
        if stack:
            return False
        return True