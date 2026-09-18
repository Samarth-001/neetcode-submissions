class StockSpanner:

    def __init__(self):
        self.st=[]        

    def next(self, price: int) -> int:
        span = 1
        # print(self.st)
        while self.st and (self.st[-1][0]<=price):
            p, sp = self.st.pop()
            span+=sp
        
        self.st.append([price, span])
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)