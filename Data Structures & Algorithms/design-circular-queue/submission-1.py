class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class MyCircularQueue:

    def __init__(self, k: int):
        self.head = dummy = ListNode()
        for _ in range(k):
            dummy.next = ListNode()
            dummy = dummy.next
        
        self.head = self.head.next
        self.tail = dummy
        self.tail.next = self.head
        self.size = 0
        self.k = k

    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            self.tail.next.val = value
            self.tail = self.tail.next
            self.size+=1
            return True
        return False

    def deQueue(self) -> bool:
        if not self.isEmpty():
            self.head.val = None
            self.head = self.head.next
            self.size-=1
            return True
        return False

    def Front(self) -> int:
        if self.head.val!=None:
            return self.head.val
        return -1

    def Rear(self) -> int:
        if self.tail.val!=None:
            return self.tail.val
        return -1

    def isEmpty(self) -> bool:
        if self.size == 0:
            return True
        return False

    def isFull(self) -> bool:
        if self.size == self.k:
            return True
        return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()