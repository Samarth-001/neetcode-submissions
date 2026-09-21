# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow = head
        fast = slow.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        print(slow.val)

        prev = None
        curr = slow.next
        slow.next = None

        while (curr!= None):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        while prev:
            first_next = head.next
            second_next = prev.next

            head.next = prev
            prev.next = first_next

            head = first_next
            prev = second_next