class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for ch in tokens:
            if ch not in {"+", "-", "*", "/"}:
                stack.append(int(ch))

            elif ch == "+":
                el1 = stack.pop()
                el2 = stack.pop()
                stack.append(el2 + el1)

            elif ch == "-":
                el1 = stack.pop()
                el2 = stack.pop()
                stack.append(el2 - el1)

            elif ch == "*":
                el1 = stack.pop()
                el2 = stack.pop()
                stack.append(el2 * el1)

            elif ch == "/":
                el1 = stack.pop()
                el2 = stack.pop()
                stack.append(int(el2 / el1))  # truncate toward 0

        return stack[-1]