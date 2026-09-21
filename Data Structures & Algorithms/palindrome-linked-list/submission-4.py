# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        length = 0
        curr = head

        while curr:
            length += 1
            curr = curr.next
        
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        print(slow.val, length)
        if slow.next == None:
            if head.next==None or head.val == head.next.val:
                return True
            return False

        if length%2 == 1:
            shead = slow.next
            slow.next = None
        else:
            shead = slow

        prev = None
        curr = shead

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        while prev:
            if prev.val != head.val:
                return False
            
            prev = prev.next
            head = head.next
        
        return True
