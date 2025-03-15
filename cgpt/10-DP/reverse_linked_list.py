class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseListIterative(head: ListNode) -> ListNode:
    prev, curr = None, head

    while curr:
        next_node = curr.next  # Store next node
        curr.next = prev       # Reverse pointer
        prev = curr            # Move prev forward
        curr = next_node       # Move curr forward

    return prev  # New head of reversed list
