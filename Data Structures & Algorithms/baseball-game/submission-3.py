class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        stack = []

        for op in operations:
            if op.lstrip("-").isdigit()  == True:
                # if stack:
                    # stack.append(stack[-1]+int(op))
                # else:
                stack.append(int(op))
            elif op == "D":
                if stack:
                    stack.append(stack[-1]*2)
            elif op == "C":
                if stack:
                    stack.pop()
            elif op=="+":
                if not stack:
                    stack.append(0)
                stack.append(stack[-1] + stack[-2])
            print(stack)
            
        
        sum = 0
        for i in range(len(stack)):
            sum+=stack[i]
        return sum        