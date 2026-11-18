# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def merge_sort(head):
    if head is None or head.next is None:
        return head

    mid = find_middle(head)

    left = head
    right = mid.next
    mid.next = None

    left = merge_sort(left)
    right = merge_sort(right)

    sorted_list = merge(left, right)
    return sorted_list

def find_middle(head):
    slow = head
    fast = head

    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next

    return slow

def merge(left, right):
    dummy = ListNode()
    current = dummy

    while left is not None and right is not None:
        if left.val < right.val:
            current.next = left
            left = left.next
        else:
            current.next = right
            right = right.next

        current = current.next

    if left is not None:
        current.next = left
    elif right is not None:
        current.next = right

    return dummy.next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return merge_sort(head)
