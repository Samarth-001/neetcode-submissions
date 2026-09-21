# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if list1 == None:
            return list2
        elif list2 == None:
            return list1
            
        head1 = list1
        head2 = list2

        curr = None
        
        if head1.val<head2.val:
            curr = head1
            ret = curr
            head1 = head1.next
        else:
            curr = head2
            ret = curr
            head2 = head2.next

        while head1!= None and head2!= None:
            if head1.val<head2.val:
                curr.next = head1
                head1 = head1.next
            else:
                curr.next = head2
                head2 = head2.next

            curr = curr.next
        
        if head1:
            curr.next = head1
        if head2:
            curr.next = head2
        
        return ret