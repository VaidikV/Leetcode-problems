def reverseLinkedList(self):

    prev = None
    curr = head

    while curr is not None:
        next_pointer = curr.next
        curr.next = prev

        prev = curr
        curr = next_pointer
    return prev
