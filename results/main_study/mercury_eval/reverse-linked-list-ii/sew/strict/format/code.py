# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        if right == left:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        for _ in range(0, left - 1):
            prev = prev.next

        current = prev.next
        next_node = current.next

        for _ in range(0, right - left):
            current.next = next_node.next
            next_node.next = prev.next
            prev.next = next_node
            next_node = current.next
        return dummy.next
