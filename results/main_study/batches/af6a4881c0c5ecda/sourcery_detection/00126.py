# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Count the total elements in the list.
        ptr = head
        total = 0
        while ptr:
            total += 1
            ptr = ptr.next

        if k > total or k <= 1:
            return head

        nb_block = total // k

        rev_head = head
        ptr = head
        count = 0
        count_block = 0
        final_head = None
        last_head = None

        while ptr.next:
            rev_ptr = rev_head
            rev_head = ptr.next
            ptr.next = ptr.next.next
            rev_head.next = rev_ptr
            count += 1
            # print("rv:", rev_head)
            if count == k - 1:
                count_block += 1
                count = 0
                if count_block == 1:
                    final_head = rev_head
                else:
                    last_head.next = rev_head
                last_head = ptr
                # print("--> lh:", last_head)
                # print("=> fi:", final_head)

                ptr = ptr.next
                rev_head = ptr

            if count_block == nb_block:
                break

        return final_head
