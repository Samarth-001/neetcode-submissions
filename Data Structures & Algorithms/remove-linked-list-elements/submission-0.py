# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        curr = ListNode()
        point = curr 
        curr.next = head
        next = curr.next
        
        while next:
            while next and next.val == val:
                next = next.next
            
            curr.next = next
            curr = next
            next = curr.next if curr else None
        
        return point.next