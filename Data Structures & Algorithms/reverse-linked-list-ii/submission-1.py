# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        dummy = ListNode()
        dummy.next = head

        lprev = dummy

        for _ in range(left-1):
            lprev = lprev.next
        
        l, r = lprev.next, lprev.next

        for _ in range(right - left):
            r = r.next

        rafter = r.next

        prev = l
        curr = l.next

        for _ in range(right - left):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        lprev.next = r
        l.next = rafter

        return dummy.next