class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        self.q1.append(x)


    def pop(self) -> int:
        le = len(self.q1)
        r = 0
        while(r<le-1):
            self.q2.append(self.q1.popleft())
            r+=1
        r = self.q1.popleft()
        self.q2, self.q1 = self.q1, self.q2
        return r

    def top(self) -> int:
        le = len(self.q1)
        return self.q1[le-1]

    def empty(self) -> bool:
        return not bool(self.q1)
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()