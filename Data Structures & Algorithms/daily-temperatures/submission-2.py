class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        st = []
        ans = []
        for i in range(len(temperatures)-1, -1, -1):
            # print(st)
            while st and (temperatures[i]>=temperatures[st[-1]]):
                st.pop()
            if st:
                ans.append(st[-1]-i)
                st.append(i)
            else:
                ans.append(0)
                st.append(i)
        
        # print(st)
        ans = ans[::-1]
        # ans =ans.reverse()
        # print("ans here", ans)
        return ans