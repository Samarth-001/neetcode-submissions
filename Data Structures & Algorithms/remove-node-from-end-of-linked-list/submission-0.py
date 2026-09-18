# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):

        length = 0
        curr = head

        while curr:
            length += 1
            curr = curr.next

        target = length - n

        # remove head
        if target == 0:
            return head.next

        curr = head

        for _ in range(target - 1):
            curr = curr.next

        curr.next = curr.next.next

        return head