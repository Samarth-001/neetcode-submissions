# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        check = head
        l = 0

        while check:
            l+=1
            check = check.next
        
        k = l -n-1

        if k == -1:
            return head.next
        i = 0
        check = head
        while i<k:
            i+=1
            check = check.next

        prev = check
        curr = check.next

        prev.next = curr.next
        return head