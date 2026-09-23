# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        slow = fast = head

        st = []

        st.append(slow.val)
        
        while fast and fast.next.next:
            slow = slow.next
            st.append(slow.val)
            fast = fast.next.next

        slow = slow.next
        # print(st)
        sum = 0
        while slow:
            sum = max(sum, (slow.val+st.pop()))
            slow = slow.next
        
        # print(sum)
        return sum