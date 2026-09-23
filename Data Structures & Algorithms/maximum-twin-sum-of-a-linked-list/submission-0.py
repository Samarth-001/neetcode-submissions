# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        slow = fast = head

        while fast and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        shead = slow.next
        prev = None
        curr = shead

        while curr:
            print("curry val",curr.val)
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        sum = 0
        while prev:
            sum = max(sum, (prev.val+head.val))
            prev = prev.next
            head = head.next

        return sum