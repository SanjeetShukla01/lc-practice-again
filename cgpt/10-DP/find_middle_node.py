class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def findMiddleNode(head: ListNode) -> ListNode:
    slow, fast = head, head  # Both pointers start at head

    while fast and fast.next:  # Move fast by 2 steps, slow by 1 step
        slow = slow.next
        fast = fast.next.next

    return slow  # Slow is now at the middle node


