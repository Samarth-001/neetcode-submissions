class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        pass

        output = [0]*len(prices)

        st = []

        for i in range((len(prices)-1),-1,-1):
            while st and st[-1]>prices[i]:
                st.pop()

            if not st:
                st.append(prices[i])
                output[i] = prices[i]
            else:
                output[i] = prices[i]-st[-1]
                st.append(prices[i])
        
        return output