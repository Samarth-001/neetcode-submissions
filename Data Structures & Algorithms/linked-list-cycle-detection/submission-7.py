# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if head == None:
            return False

        l = head
        r = l.next

        if r == None:
            return False


        while r and r.next and l!=r:
            l = l.next
            r = r.next.next
        
        if l == r:
            return True
        return False
        