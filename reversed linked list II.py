class Solution:
    def reverseBetween(self, head, left, right):
        dummy = ListNode(0, head)
        left_prev, cur = dummy, head
        for i in range(left -1):
            left_prev, cur = cur, cur.next

        prev = None
        for i in range(right - left + 1):
            tmp_next = cur.next
            cur.next = prev
            prev, cur = cur, tmp_next

        left_prev.next.next = cur
        left_prev.next = prev
        return dummy.next


