class Solution:
    def reorderList(self, head):

        if not head or not head.next:
            return

        # -------------------------
        # Find middle of list
        # -------------------------
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # -------------------------
        # Reverse second half
        # -------------------------
        prev = None
        curr = slow.next
        slow.next = None

        while curr:
            next_node = curr.next

            curr.next = prev

            prev = curr
            curr = next_node

        # prev is head of reversed second half

        # -------------------------
        # Merge two halves
        # -------------------------
        first = head
        second = prev

        while second:

            first_next = first.next
            second_next = second.next

            first.next = second
            second.next = first_next

            first = first_next
            second = second_next