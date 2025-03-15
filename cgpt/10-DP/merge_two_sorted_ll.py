class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode()  # Dummy node to start the merged list
    current = dummy  # Pointer to track the last node

    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next  # Move current pointer

    # Append remaining nodes (if any)
    current.next = l1 if l1 else l2

    return dummy.next  # Return the merged list, skipping the dummy node
