from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]
) -> Optional[ListNode]:
    dummy = ListNode()
    carry, curr = 0, dummy
    while l1 or l2 or carry:
        s = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
        carry, val = divmod(s, 10)
        curr.next = ListNode(val)
        curr = curr.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    return dummy.next



def new_two_sum(l1, l2):

    dummy_head = ListNode(0)
    current = dummy_head
    carry = 0

    while l1 or l2 or carry:
        x = l1.val if l1 else 0
        y = l2.val if l2 else 0

        total = x + y + carry
        print(f"total: {total}")
        carry = total // 10
        print(f"carry: {carry}")
        digit = total % 10
        print(f"digit: {digit}")

        current.next = ListNode(digit)
        current = current.next

        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    return dummy_head.next

if __name__ == '__main__':
    # Example usage:
    # Create linked lists:
    l1 = ListNode(2, ListNode(4, ListNode(3)))  # Represents 342
    l2 = ListNode(5, ListNode(6, ListNode(4)))  # Represents 465

    result = new_two_sum(l1, l2)
    print(result.val)

    # Print the result linked list:
    while result:
        print(result.val, end=" -> ")
        result = result.next
    print("None")  # Output: 7 -> 0 -> 8 -> None