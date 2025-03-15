class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def hasCycle(head: ListNode) -> bool:
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next  # Move slow pointer by 1 step
        fast = fast.next.next  # Move fast pointer by 2 steps

        if slow == fast:  # If they meet, a cycle exists
            return True

    return False  # No cycle detected



# O(n) – We traverse the linked list once.
