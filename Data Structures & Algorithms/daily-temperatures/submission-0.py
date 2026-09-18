class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        ans = [0] * len(temperatures)

        for i, num in enumerate(temperatures):
            print("num", num)
            print("stack", stack)
            print("output", ans)
            
            if not stack:
                stack.append(i)
                continue

                
            while stack and temperatures[stack[-1]] < num:
                ans[stack[-1]] = (i-stack[-1])
                stack.pop()
            
            stack.append(i)
        
        return ans